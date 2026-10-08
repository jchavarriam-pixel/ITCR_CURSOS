Add-Type -AssemblyName System.Speech
$modelRoot = $PSScriptRoot
$modelManifest = Get-Content -LiteralPath (Join-Path $modelRoot 'audios/guiones.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$modelTimings = @{}
$modelTimingPath = Join-Path $modelRoot 'audios/animaciones-modelos.json'
if (Test-Path -LiteralPath $modelTimingPath) {
    $modelSavedTimings = Get-Content -LiteralPath $modelTimingPath -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($modelSavedVoice in $modelSavedTimings.PSObject.Properties) { $modelTimings[$modelSavedVoice.Name] = $modelSavedVoice.Value }
}
$modelSpeaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$modelEventId = 'Regresion.ModelNarration.Bookmarks'
Register-ObjectEvent -InputObject $modelSpeaker -EventName BookmarkReached -SourceIdentifier $modelEventId | Out-Null
try {
    foreach ($modelVoice in $modelManifest.voces) {
        if ($modelVoice.tipo -eq 'neural') { continue }
        $modelSpeaker.SelectVoice($modelVoice.voz)
        $modelTimings[$modelVoice.id] = @{}
        $modelVoiceDirectory = Join-Path $modelRoot 'audios'
        if ($modelVoice.carpeta) { $modelVoiceDirectory = Join-Path $modelVoiceDirectory $modelVoice.carpeta }
        foreach ($modelClip in $modelManifest.paginas.formas) {
            if ($modelClip.id -ne 'modelos-no-lineales' -and $modelClip.id -notlike 'modelo-*') { continue }
            $modelSentences = [regex]::Split($modelClip.texto, '(?<=[.!?])\s+')
            $modelSsml = '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="es-ES">'
            for ($modelSentenceIndex = 0; $modelSentenceIndex -lt $modelSentences.Count; $modelSentenceIndex++) {
                $modelSsml += '<mark name="s' + $modelSentenceIndex + '"/>' + [System.Security.SecurityElement]::Escape($modelSentences[$modelSentenceIndex]) + ' '
            }
            $modelSsml += '<mark name="end"/></speak>'
            $modelSpeaker.SetOutputToWaveFile((Join-Path $modelVoiceDirectory $modelClip.archivo))
            $modelSpeaker.SpeakSsml($modelSsml)
            $modelSpeaker.SetOutputToNull()
            $modelEvents = @(Get-Event -SourceIdentifier $modelEventId -ErrorAction SilentlyContinue)
            $modelTimings[$modelVoice.id][$modelClip.id] = @($modelEvents | ForEach-Object {
                @{ mark = $_.SourceEventArgs.Bookmark; time = [math]::Round($_.SourceEventArgs.AudioPosition.TotalSeconds, 3) }
            })
            $modelEvents | Remove-Event
            if ($modelTimings[$modelVoice.id][$modelClip.id].Count -lt 2) { throw "No se registraron las marcas de $($modelClip.id)." }
        }
    }
    $modelJson = $modelTimings | ConvertTo-Json -Depth 8 -Compress
    Set-Content -LiteralPath (Join-Path $modelRoot 'audios/animaciones-modelos.json') -Value $modelJson -Encoding UTF8
    $modelHtmlPath = Join-Path $modelRoot 'regresion_interactiva.html'
    $modelHtml = [System.IO.File]::ReadAllText($modelHtmlPath)
    $modelOld = [regex]::Match($modelHtml, 'const modelNarrationTimings=.*;')
    if ($modelOld.Success) {
        $modelHtml = $modelHtml.Replace($modelOld.Value, 'const modelNarrationTimings=' + $modelJson + ';')
        [System.IO.File]::WriteAllText($modelHtmlPath, $modelHtml, [System.Text.UTF8Encoding]::new($false))
    }
} finally {
    Unregister-Event -SourceIdentifier $modelEventId -ErrorAction SilentlyContinue
    Get-Event -SourceIdentifier $modelEventId -ErrorAction SilentlyContinue | Remove-Event
    $modelSpeaker.Dispose()
}

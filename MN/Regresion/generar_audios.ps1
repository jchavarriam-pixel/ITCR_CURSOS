Add-Type -AssemblyName System.Speech
$regressionAudioRoot = Join-Path $PSScriptRoot 'audios'
$regressionScripts = Get-Content -LiteralPath (Join-Path $regressionAudioRoot 'guiones.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$regressionSpeaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
    $regressionSpeaker.Rate = 0
    foreach ($regressionVoice in $regressionScripts.voces) {
        $regressionSpeaker.SelectVoice($regressionVoice.voz)
        $regressionVoiceRoot = $regressionAudioRoot
        if ($regressionVoice.carpeta) {
            $regressionVoiceRoot = Join-Path $regressionAudioRoot $regressionVoice.carpeta
            New-Item -ItemType Directory -Path $regressionVoiceRoot -Force | Out-Null
        }
        foreach ($regressionPage in $regressionScripts.paginas.PSObject.Properties) {
            foreach ($regressionClip in $regressionPage.Value) {
                $regressionOutput = Join-Path $regressionVoiceRoot ($regressionClip.id + '.wav')
                $regressionSpeaker.SetOutputToWaveFile($regressionOutput)
                $regressionSpeaker.Speak($regressionClip.texto)
                $regressionSpeaker.SetOutputToNull()
            }
        }
        Write-Output ($regressionVoice.nombre + ': audios generados')
    }
} finally {
    $regressionSpeaker.Dispose()
}
& (Join-Path $PSScriptRoot 'generar_animaciones.ps1')

"""Genera las voces adicionales. Requiere: python -m pip install edge-tts.

La síntesis envía los guiones al servicio de voz de Microsoft.
Los MP3 resultantes se reproducen después sin conexión.
"""
import asyncio
import json
import re
from pathlib import Path
import edge_tts

ROOT = Path(__file__).resolve().parent
VOICES = [
    dict(id="juan", nombre="Juan · Costa Rica · masculina", voz="es-CR-JuanNeural", carpeta="juan", tipo="neural", extension="mp3"),
    dict(id="maria", nombre="María · Costa Rica · femenina", voz="es-CR-MariaNeural", carpeta="maria", tipo="neural", extension="mp3"),
    dict(id="jorge", nombre="Jorge · México · masculina", voz="es-MX-JorgeNeural", carpeta="jorge", tipo="neural", extension="mp3"),
]

async def main():
    manifest_path = ROOT / "audios/guiones.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    timing_path = ROOT / "audios/animaciones-modelos.json"
    timings = json.loads(timing_path.read_text(encoding="utf-8-sig"))
    semaphore = asyncio.Semaphore(3)
    clips = [clip for page in manifest["paginas"].values() for clip in page]
    animated = {clip["id"] for clip in manifest["paginas"]["formas"] if clip["id"] == "modelos-no-lineales" or clip["id"].startswith("modelo-")}
    completed = 0

    async def generate(voice, clip):
        nonlocal completed
        folder = ROOT / "audios" / voice["carpeta"]
        folder.mkdir(exist_ok=True)
        target = folder / Path(clip["archivo"]).with_suffix(".mp3")
        async with semaphore:
            for attempt in range(4):
                try:
                    marks = []
                    with target.with_suffix(".tmp").open("wb") as audio:
                        async for event in edge_tts.Communicate(clip["texto"], voice["voz"], boundary="SentenceBoundary").stream():
                            if event["type"] == "audio":
                                audio.write(event["data"])
                            elif event["type"] == "SentenceBoundary":
                                marks.append(dict(mark=f"s{len(marks)}", time=round(event["offset"] / 10_000_000, 3)))
                                end = (event["offset"] + event["duration"]) / 10_000_000
                    if not marks or target.with_suffix(".tmp").stat().st_size == 0:
                        raise RuntimeError("No se recibió el audio completo")
                    if clip["id"] in animated:
                        expected = len(re.split(r"(?<=[.!?])\s+", clip["texto"].strip()))
                        if len(marks) != expected:
                            raise RuntimeError(f"Marcas de frases: {len(marks)}, esperadas: {expected}")
                        marks.append(dict(mark="end", time=round(end, 3)))
                        timings.setdefault(voice["id"], {})[clip["id"]] = marks
                    target.with_suffix(".tmp").replace(target)
                    completed += 1
                    if completed % 12 == 0:
                        print(f"Audios generados: {completed}/{len(clips) * len(VOICES)}", flush=True)
                    break
                except Exception:
                    if attempt == 3:
                        raise
                    await asyncio.sleep(2 * (attempt + 1))

    await asyncio.gather(*(generate(voice, clip) for voice in VOICES for clip in clips))
    manifest["voces"] = [voice for voice in manifest["voces"] if voice["id"] not in {v["id"] for v in VOICES}] + VOICES
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    timing_path.write_text(json.dumps(timings, ensure_ascii=False), encoding="utf-8")
    html_path = ROOT / "regresion_interactiva.html"
    html = html_path.read_text(encoding="utf-8")
    for variable, value in [("lessonAudioVoices", manifest["voces"]), ("modelNarrationTimings", timings)]:
        html = re.sub(r"const " + variable + r"=.*;", lambda _: "const " + variable + "=" + json.dumps(value, ensure_ascii=False) + ";", html)
    html_path.write_text(html, encoding="utf-8")
    print("Voces y tiempos de animación actualizados.", flush=True)

if __name__ == "__main__":
    asyncio.run(main())

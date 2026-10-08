"""Comprueba los recursos del documento y, opcionalmente, crea un ZIP publicable."""
import argparse
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def check_exact_path(relative):
    current = ROOT
    for part in Path(relative).parts:
        if not current.is_dir() or part not in {item.name for item in current.iterdir()}:
            raise ValueError(f"Falta el archivo o su nombre no coincide exactamente: {relative}")
        current /= part
    if not current.is_file() or (current.stat().st_size == 0 and current.name != ".nojekyll"):
        raise ValueError(f"Archivo vacío o no válido: {relative}")
    if current.stat().st_size >= 100 * 1024 * 1024:
        raise ValueError(f"El archivo supera el tamaño permitido para Git: {relative}")
    return current


def publication_files():
    files = ["index.html", "regresion_interactiva.html", ".nojekyll",
             "Como_predecir_el_futuro_con_regresion.m4a"]
    manifest = json.loads((ROOT / "audios/guiones.json").read_text(encoding="utf-8-sig"))
    clip_files = {clip["archivo"] for clips in manifest["paginas"].values() for clip in clips}
    for voice in manifest["voces"]:
        folder = Path("audios") / voice.get("carpeta", "")
        files.extend((folder / Path(filename).with_suffix("." + voice.get("extension", "wav"))).as_posix() for filename in sorted(clip_files))
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", action="store_true", help="Crear publicacion/regresion-web.zip")
    args = parser.parse_args()
    try:
        files = publication_files()
        checked = [check_exact_path(relative) for relative in files]
        html = (ROOT / "regresion_interactiva.html").read_text(encoding="utf-8")
        if "file:///" in html or "C:/Users/" in html or "C:\\Users\\" in html:
            raise ValueError("El documento contiene una ruta local absoluta que no funcionará en la web.")
        print(f"Publicación comprobada: {len(files)} archivos, "
              f"{sum(item.stat().st_size for item in checked) / 1024**2:.1f} MB.")
        if args.zip:
            destination = ROOT / "publicacion" / "regresion-web.zip"
            destination.parent.mkdir(exist_ok=True)
            with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                for relative, source in zip(files, checked):
                    archive.write(source, relative)
            print(f"Paquete creado: {destination}")
    except (OSError, ValueError, KeyError) as error:
        print(f"No se puede publicar todavía: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

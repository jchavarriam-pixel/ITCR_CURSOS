# Regresión · Métodos Numéricos

Documento interactivo en español del Prof. Jeffry Chavarría Molina, Escuela de Matemática, Instituto Tecnológico de Costa Rica.

Incluye navegación por páginas, actividades con comprobación, gráficas interactivas, glosario matemático y explicaciones de audio. No requiere instalar bibliotecas ni ejecutar un servidor para estudiar el contenido.

## Publicar en el repositorio ITCR_CURSOS

1. En GitHub Desktop, guarda los cambios de esta carpeta mediante **Commit** y pulsa **Push origin**. Incluye el HTML, la página de entrada, la carpeta `audios` completa y el archivo `Como_predecir_el_futuro_con_regresion.m4a`. También puedes usar los comandos indicados más abajo.
2. Abre [Settings → Pages del repositorio](https://github.com/jchavarriam-pixel/ITCR_CURSOS/settings/pages).
3. En **Build and deployment**, elige **Deploy from a branch** como origen, la rama **main** y la carpeta **/(root)**. Guarda la configuración. Si estos valores ya están seleccionados, no hace falta cambiarlos.
4. Espera a que termine el despliegue en la pestaña **Actions**. GitHub mostrará la dirección publicada en **Settings → Pages**.
5. Abre la dirección del documento y prueba un audio y el pódcast.

La dirección prevista para este repositorio es:

**https://jchavarriam-pixel.github.io/ITCR_CURSOS/MN/Regresion/**

También se puede compartir una página concreta, por ejemplo:

**https://jchavarriam-pixel.github.io/ITCR_CURSOS/MN/Regresion/#linealizacion**

La entrada de regresión conserva el fragmento y abre `regresion_interactiva.html`. La entrada principal del repositorio sigue llevando a matrices. El archivo `.nojekyll` de la raíz del repositorio ya permite servir el sitio como archivos estáticos.

Desde la **raíz del repositorio**, la alternativa con Git es:

```powershell
git add -- MN/Regresion
git commit -m "Añadir documento interactivo de regresión"
git push origin main
```

GitHub Desktop o Git permiten subir el pódcast, cuyo tamaño supera el límite de carga individual de la interfaz web de GitHub. No hace falta utilizar Git LFS para estos archivos.

## Comprobar los archivos antes de publicar

Desde esta carpeta:

```powershell
python verificar_publicacion.py
```

El verificador comprueba la entrada, el documento, el pódcast y todos los audios de las voces disponibles. También comprueba las mayúsculas y minúsculas de los nombres, porque las rutas publicadas deben coincidir exactamente.

## Preparar un paquete para otro sitio o un repositorio independiente

```powershell
python verificar_publicacion.py --zip
```

Se crea `publicacion/regresion-web.zip` con la entrada, el documento, el pódcast y los audios utilizados. No incluye los PDF de referencia, las muestras de voces ni los scripts de generación. Descomprime el paquete en la carpeta que se vaya a servir como sitio web. En un repositorio independiente, selecciona **main / (root)** en GitHub Pages; su dirección será la de ese repositorio.

El ZIP se genera solo cuando se solicita y está excluido del control de versiones.

## Actualizar el contenido

Edita `regresion_interactiva.html`, comprueba los archivos y vuelve a guardar y subir los cambios. GitHub Pages actualizará el documento tras completar el despliegue.

Los guiones se mantienen en `audios/guiones.json`. En Windows, `generar_audios.ps1` regenera las voces locales y llama a `generar_animaciones.ps1` para actualizar los tiempos de las animaciones. Si cambias un guion, actualiza también los guiones integrados en el HTML. No es necesario regenerar el audio para modificar únicamente el aspecto o las fórmulas.

## Abrirlo sin conexión

Abre `index.html` o `regresion_interactiva.html`. Mantén el pódcast y la carpeta `audios` junto al HTML. El motor matemático y sus fuentes están integrados en el documento.

## Documentación de GitHub

[Configurar el origen de publicación de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

# Integración numérica

Abra **index.html**. El recorrido sigue los quince videos reales de la carpeta compartida por el profesor:

https://drive.google.com/drive/folders/1Fb1vzLbSPLfnSSsjEOxOHkl9CqQCcAJP

## Videos incorporados

Cada lección carga el reproductor de Google Drive al pulsar «Reproducir». Debajo se ofrece «Abrir video en Drive» para verlo en una pestaña independiente. No es necesario descargar ni guardar los MP4 dentro de esta carpeta. La reproducción requiere conexión a internet.

Se verificaron los nombres de los quince archivos y que todos tienen permiso de lectura para cualquier persona con el enlace. No se modificó ningún archivo ni permiso en Google Drive.

| Orden | Archivo en Drive | Duración |
| --- | --- | --- |
| 01 | `01_regla_compuesta_rectangulo.mp4` | 7:00 |
| 02 | `02_trapecio_deduccion.mp4` | 8:36 |
| 03 | `03_trapecio_ejemplo.mp4` | 4:06 |
| 04 | `04_trapecio_compuesto_deduccion.mp4` | 5:21 |
| 05 | `05_trapecio_compuesto_ejemplo.mp4` | 4:34 |
| 06 | `06_simpson_deduccion.mp4` | 6:10 |
| 07 | `07_simpson_ejemplo.mp4` | 3:34 |
| 08 | `08_simpson_error.mp4` | 5:22 |
| 09 | `09_simpson_compuesto_deduccion.mp4` | 8:18 |
| 10 | `10_simpson_compuesto_ejemplo.mp4` | 5:55 |
| 11 | `11_cuadratura_gaussiana.mp4` | 7:08 |
| 12 | `12_gauss_legendre_dos_puntos.mp4` | 9:54 |
| 13 | `13_gauss_legendre_tres_puntos.mp4` | 7:37 |
| 14 | `14_gauss_legendre_tres_ejemplo.mp4` | 5:19 |
| 15 | `15_gauss_legendre_resumen.mp4` | 3:26 |

El primer video repasa la regla compuesta del rectángulo. Los videos 02–05 cubren trapecio; 06–10, Simpson; 11–15, cuadratura gaussiana. La comparación general y el reto final quedaron incorporados a la última lección, sin crear un video adicional.

Las duraciones y la descripción temática se contrastaron con el archivo LEEME.md de la misma carpeta de Drive. Los títulos de las lecciones están redactados para el estudiante y no tienen que coincidir literalmente con los nombres de los MP4. Los identificadores internos anteriores se conservan para mantener el avance y las notas existentes.

## Estructura de cada lección

Cada video tiene una lección con la misma organización:

1. **Enunciado** (solo en los ejercicios), escrito tal como aparece en el video.
2. **Video**, que se carga al pulsar «Reproducir».
3. **Procedimiento del video** (ejercicios) o **Desarrollo escrito del video** (deducciones): los mismos renglones de la hoja del video, cada uno con su justificación a la derecha, con diez decimales y los mismos valores numéricos.
4. **Gráfica del método** (solo en los videos de explicación: 01, 02, 04, 06, 08, 09, 11, 12, 13 y 15). Se puede elegir entre siete funciones con comportamientos distintos (la del ejemplo, una que oscila, una campana, una cúbica que cambia de concavidad, √x, un pico estrecho y una oscilación creciente) y cambiar la cantidad de subintervalos o de nodos para ver qué figuras construye el método y cómo cambia el error.

La navegación lateral sigue el orden de los videos. «Marcar como visto» registra el avance solo en el navegador. Las fórmulas funcionan sin conexión gracias a la copia local de KaTeX; los videos requieren internet.

## Archivos

- `index.html`: estructura de la página.
- `videos.js`: los quince videos de Drive (identificadores, duraciones y direcciones de inserción).
- `contenido.js`: enunciados, procedimientos y desarrollos de cada video.
- `app.js`: navegación, reproductor, avance y gráficas de exploración.
- `ejes.js`: marco cartesiano de las gráficas (ejes en cero).
- `estilos.css`: diseño para computadora, teléfono e impresión.
- `assets/`: KaTeX y su licencia. `materiales/`: PDF de las notas de clase.
- `guia-videos.js`: versión anterior de los textos; ya no se carga y puede borrarse.

Para sustituir un video, edite su entrada en `videos.js`. La carpeta es un sitio estático que puede alojarse en GitHub Pages; no necesita compilarse.

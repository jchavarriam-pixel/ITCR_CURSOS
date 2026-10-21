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

## Uso y navegación

Los títulos, las descripciones y los puntos de seguimiento se adaptaron a las descripciones completas de los quince videos aportadas por el profesor. Se incorporaron el cálculo de la cantidad de rectángulos a partir de la tolerancia, las integrales auxiliares del trapecio, la deducción de Simpson mediante Newton, los sistemas de exactitud, los límites de las sumatorias y los dos ejemplos del resumen. Las tablas de los ejercicios muestran diez decimales por defecto; algunas comparaciones de errores conservan más cifras para que el redondeo no las oculte.

El índice permite consultar cualquier tema. «Anterior» y «Siguiente» siguen el orden real de los videos. Las gráficas permiten cambiar particiones y nodos manteniendo los ejes fijos. Las actividades aceptan coma o punto decimal. El avance y las notas personales se guardan únicamente en el navegador. «Marcar como visto» sirve para registrar el avance de los videos de Drive, cuyo estado de reproducción no es accesible desde el documento por tratarse de un reproductor externo.

Las fórmulas y el contenido escrito funcionan sin conexión gracias a la copia local de KaTeX. Los videos sí requieren internet. Las sumas se componen con displaystyle.

## Cotas y contenido matemático

Se cubren los ejercicios de las notas y se incluye un repaso de rectángulos para acompañar el primer video. Se utiliza la convención error con signo = integral − aproximación. Las referencias numéricas de calculadora no se presentan como valores exactos.

Para seguir las grabaciones, se usan las cotas dadas M₂ = 0,24 y M₄ = 0,14 para la función sen(x)/x en el intervalo de uno a dos. Se actualizaron las cotas de trapecio, trapecio compuesto, Simpson y Simpson compuesto con esos mismos valores. Los cálculos internos conservan la precisión; el redondeo se realiza al mostrar.

Las fuentes originales revisadas fueron S12 Cls.tex y S12 Cls (Visto en S13).pdf, ubicados en C:/Users/jeffz/OneDrive/ITCR/2026/IIS26/Cursos/MN/Notas de clase MN/S12/. La copia de consulta del PDF está en materiales/notas-de-clase.pdf y no se modificó.

Se mantuvieron las correcciones editoriales de la adaptación: el cambio de variable se usa para un intervalo distinto de menos uno a uno; el ejemplo que sigue a Gauss de tres puntos se resuelve con tres puntos, aunque el enunciado original repite «dos puntos».

## Configuración y traslado

- videos.js: los quince archivos, sus identificadores de Drive, las duraciones y las direcciones de inserción.
- contenido.js: lecciones, datos, fórmulas y cálculos.
- guia-videos.js: adaptación de títulos, puntos de seguimiento, deducciones y ejercicios a las descripciones definitivas de los quince videos.
- ejes.js: marco cartesiano común; el eje vertical pasa por x = 0 y el horizontal por y = 0. Las ventanas incluyen el origen sin modificar el intervalo de integración ni los cálculos.

Las curvas se prolongan un 20 % de la longitud del intervalo a cada lado. Las áreas y las aproximaciones se mantienen entre los límites de integración. La ventana y, cuando hace falta, la escala vertical se calculan de modo que se vean las prolongaciones, conservando los ejes en cero. Los controles de particiones no cambian la escala.
- app.js: navegación, reproductores, gráficas, comprobaciones y notas.
- estilos.css: diseño para computadora y teléfono.
- assets/: KaTeX y su licencia.
- materiales/: PDF de consulta.

Para sustituir un video, edite su entrada en videos.js. También se admite tipo:'archivo' con una ruta a un MP4 local, o tipo:'iframe' con una dirección válida de inserción. Si configura un video local, puede añadir subtitulos:'videos/nombre.es.vtt'.

La carpeta completa es un sitio estático que puede alojarse en GitHub Pages o trasladarse a otro equipo. No necesita compilarse. El ZIP contiene el documento y sus enlaces, sin incluir las grabaciones. Este cambio actualiza la copia local; no publica un sitio nuevo.

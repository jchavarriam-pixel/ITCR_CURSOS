# Integración numérica

Abra **index.html**. La guía funciona en español y sin conexión: las fórmulas usan una copia local de KaTeX. Para los videos hacen falta los archivos multimedia, o una conexión si se usan videos alojados en otro servicio.

## Organización

- Videos 01–04: trapecio simple y compuesto, deducciones, errores y ejemplos.
- Videos 05–09: Simpson simple y compuesto, precisión y ejemplos.
- Videos 10–15: cuadratura gaussiana, Gauss-Legendre de dos, tres y cuatro puntos y comparación final.

El índice siempre permite navegar libremente. «Anterior» y «Siguiente» siguen el orden propuesto. El avance y las notas se guardan localmente en cada navegador; no se envían a un servidor. El botón para reiniciar el avance conserva las notas personales.

## Incorporar los videos

Los primeros once identificadores y su orden son exactamente los suministrados por el profesor. Hay quince espacios en total. Como se suministraron once nombres, los cuatro últimos son una propuesta basada en el contenido restante de las notas, no títulos confirmados de archivos existentes:

| Orden | Archivo esperado dentro de `videos/` | Contenido |
| --- | --- | --- |
| 01 | `09_trapecio_deduccion.mp4` | Interpolante lineal, valor medio ponderado, error y geometría |
| 02 | `10_trapecio_ejemplo.mp4` | Integral trigonométrica con un trapecio |
| 03 | `11_trapecio_compuesto_deduccion.mp4` | Suma de trapecios y error compuesto |
| 04 | `12_trapecio_compuesto_ejemplo.mp4` | Partición de tres subintervalos |
| 05 | `13_simpson_deduccion.mp4` | Integración del interpolante cuadrático |
| 06 | `14_simpson_ejemplo.mp4` | Ejemplo de Simpson simple |
| 07 | `15_simpson_error.mp4` | Exactitud cúbica y cota de error |
| 08 | `16_simpson_compuesto_deduccion.mp4` | Pesos alternados, cantidad par de subintervalos |
| 09 | `17_simpson_compuesto_ejemplo.mp4` | Tabla de once nodos |
| 10 | `18_cuadratura_gaussiana.mp4` | Elección de nodos y grado de precisión |
| 11 | `19_gauss_legendre_dos_puntos.mp4` | Deducción, cúbica, cambio de variable y los dos ejemplos no polinómicos |
| 12 | `20_gauss_legendre_tres_puntos.mp4` | Fórmula y justificación de tres puntos (propuesto) |
| 13 | `21_gauss_legendre_tres_puntos_ejemplo.mp4` | Integral trigonométrica con tres puntos (propuesto) |
| 14 | `22_gauss_legendre_cuatro_puntos.mp4` | Tabla y aplicación de cuatro puntos (propuesto) |
| 15 | `23_comparacion_y_cierre.mp4` | Comparación y síntesis (propuesto) |

Copie los archivos en `videos/` con esos nombres. Use MP4 con video H.264 y audio AAC para una compatibilidad amplia. No se han creado ni simulado videos reales. Los reproductores se cargan al pulsar reproducir y muestran un mensaje claro si el archivo todavía no existe.

También puede editar **videos.js** y cambiar `src` por otra ruta o URL. Para YouTube, use `tipo:'iframe'` con una URL de inserción `https://www.youtube-nocookie.com/embed/ID`. Para Vimeo, `https://player.vimeo.com/video/ID`. No use la dirección normal de visualización en un iframe. Para subtítulos en videos locales, puede añadir `subtitulos:'videos/nombre.es.vtt'` a la entrada correspondiente. Los videos incrustados permiten marcar el avance manualmente; un MP4 local también se marca como visto al terminar.

Los números del índice son el orden de estudio, del 01 al 15. Los prefijos 09–23 de los archivos son identificadores de medios y no alteran ese orden.

## Fuentes y criterios matemáticos

Se revisaron el PDF de 14 páginas **S12 Cls (Visto en S13).pdf** y el fuente **S12 Cls.tex**, ubicados en `C:/Users/jeffz/OneDrive/ITCR/2026/IIS26/Cursos/MN/Notas de clase MN/S12/`. Una copia sin modificaciones del PDF está en `materiales/notas-de-clase.pdf`.

Se cubren todos los ejercicios: trapecio simple, trapecio compuesto con la partición dada, Simpson simple, Simpson compuesto con diez subintervalos, Gauss de dos puntos para la cúbica y para las dos integrales no polinómicas, y el ejemplo que sigue a la regla de tres puntos. La aplicación de cuatro puntos y el reto final son apoyos didácticos añadidos.

Se corrigieron dos erratas al adaptar el texto: el encabezado del cambio de variable debe referirse a un intervalo **distinto** de menos uno a uno; el ejercicio que aparece después de Gauss de tres puntos se organiza como aplicación de **tres puntos**, aunque el enunciado original repite «dos puntos». No se modificaron los originales.

Convención: error con signo = integral − aproximación. Las comparaciones de calculadora se presentan como referencias numéricas, no como valores exactos. Para la función sen(x)/x se usan las cotas seguras M₂ = 1/3 y M₄ = 1/5; su justificación está disponible en los detalles. Los valores se calculan con precisión completa y se redondean al mostrar. Las sumas usan displaystyle.

## Publicación o traslado

La carpeta completa es un sitio estático. Conserve juntos `index.html`, los tres archivos JavaScript, `estilos.css`, `assets/`, `materiales/` y `videos/`. No hace falta instalar dependencias ni compilar. Puede publicarse en cualquier alojamiento estático, incluido GitHub Pages. Este trabajo se entrega localmente; no se ha realizado una publicación nueva.

Los videos grandes pueden exceder los límites de un repositorio. En ese caso, alójelos en un servicio de video y configure sus enlaces de inserción en `videos.js`. Si solo quiere compartir el documento sin los archivos, distribuya una copia de toda la carpeta excluyendo los MP4 y use enlaces de inserción.

Para una vista HTTP local opcional, desde esta carpeta: `python -m http.server 8080`. Luego abra `http://localhost:8080/`. Un servidor en localhost solo es accesible en el equipo; no es por sí mismo un enlace público para el teléfono.

## Archivos

- `contenido.js`: lecciones, datos, fórmulas y cálculos.
- `app.js`: navegación, reproductores, gráficas, comprobaciones y notas.
- `videos.js`: configuración de los quince videos.
- `estilos.css`: diseño adaptable a computadora y teléfono.
- `assets/`: KaTeX y su licencia; las fuentes están incluidas en la hoja de estilos.
- `materiales/`: PDF de consulta.
- `videos/`: destino de los videos que se incorporarán.

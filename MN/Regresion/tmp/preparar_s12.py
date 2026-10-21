from pathlib import Path
import re, shutil
base=Path(r'C:\Users\jeffz\OneDrive\ITCR\2026\IIS26\Cursos\MN\Consignas IS26')
out=Path('tmp/orientacion-s12')
s=(base/'Orientación S12 IS26/Orientacion_S12.tex').read_text(encoding='utf-8')
shutil.copytree(base/'Orientación S12 IS26/imagenes',out/'imagenes',dirs_exist_ok=True)
shutil.copytree(base/'Direcciones',out/'Direcciones',dirs_exist_ok=True)
s=s.replace('../Direcciones/','Direcciones/')
a=s.index('La semana se estudiará')
b=s.index('{\\color{titulos}',a)
s=s[:a]+r'''La clase de la \textbf{semana 12 será asincrónica}. Trabajarán en la página web \href{https://jchavarriam-pixel.github.io/ITCR_CURSOS/MN/IntegracionNumerica/}{\textbf{Integración numérica · Métodos Numéricos}} los contenidos de las semanas 11 y 12: trapecio, Simpson y cuadratura gaussiana. Sigan el orden de las secciones: \textbf{vean primero cada video}, intenten los cálculos y luego consulten el desarrollo escrito para comparar fórmulas, procedimientos y resultados. La regla del rectángulo y su versión compuesta ya fueron estudiadas.

'''+s[b:]
a=s.index('Libro de texto:\\\\',s.index('Material a utilizar'))
b=s.index('\\vspace{0.5cm}',a)
s=s[:a]+r'''{\footnotesize
\href{https://jchavarriam-pixel.github.io/ITCR_CURSOS/MN/IntegracionNumerica/}{\textbf{Guía web de integración numérica}}\\[0.2cm]
Videos, explicaciones escritas, fórmulas, cálculos y resultados.\\[0.2cm]
Consulten también las notas de clase enlazadas en la página.
} 
'''+s[b:]
a=s.index('{{ \\tiny $\\blacksquare$}',s.index('{\\large Vídeos}'))
b=s.index('\\end{minipage}',a)
s=s[:a]+r'''{\footnotesize
\textbf{Orden de estudio:}\\[0.2cm]
\textbf{02--05:} Trapecio y trapecio compuesto.\\[0.2cm]
\textbf{06--10:} Simpson, error y Simpson compuesto.\\[0.2cm]
\textbf{11--15:} Cuadratura gaussiana y Gauss-Legendre.\\[0.2cm]
En cada sección, vean primero el video y hagan pausas para resolver por su cuenta.
}
'''+s[b:]
a=s.index('\\textbf{Esta semana:}')
b=s.index('\\end{minipage}',a)
s=s[:a]+r'''\textbf{Semana 13:}

La clase será \textbf{presencial} y se realizarán \textbf{quices sobre interpolación y regresión}.

Repasen las notas, los procedimientos y los ejercicios trabajados en ambos temas.
\vfill
'''+s[b:]
a=s.index('{ \\tiny $\\blacksquare$} Cuadratura Gaussiana')
b=s.index('{\\color{white}\\rule',a)
s=s[:a]+r'''{\footnotesize
$\blacksquare$ Trapecio simple y compuesto.\\[0.2cm]
$\blacksquare$ Simpson simple y compuesto.\\[0.2cm]
$\blacksquare$ Error real, error teórico y cotas.\\[0.2cm]
$\blacksquare$ Cuadratura gaussiana: Gauss-Legendre de 2, 3 y 4 puntos.
}

'''+s[b:]
a=s.index('{ \\tiny $\\blacksquare$} Estudiar los métodos')
b=s.index('{\\color{white}\\rule',a)
s=s[:a]+r'''{\footnotesize
$\blacksquare$ Comprender las deducciones y aplicar las reglas de integración.\\[0.2cm]
$\blacksquare$ Comparar aproximaciones y justificar cotas del error.\\[0.2cm]
$\blacksquare$ Transformar el intervalo y usar nodos y pesos de Gauss-Legendre.
}

'''+s[b:]
a=s.index('\\begin{multicols}{2}')
b=s.index('\\end{multicols}',a)+len('\\end{multicols}')
s=s[:a]+r'''\begin{multicols}{2}
Organicen el estudio por etapas. Los videos y las explicaciones escritas se complementan: los primeros muestran el proceso paso a paso y el texto permite repasar las fórmulas, los cálculos y los resultados.

{\color{actividades}\textbf{Actividad 1: Trapecio (videos 02--05)}}
\begin{itemize}
\item Estudien la deducción y el ejemplo de la regla del trapecio; luego, su versión compuesta.
\item Reproduzcan las aproximaciones de la integral de $\operatorname{sen}(x)/x$ en $[1,2]$ con uno y con tres trapecios.
\item Comparen el error real con la cota teórica. Identifiquen el papel de $h$, de $n$ y de la segunda derivada.
\end{itemize}

{\color{actividades}\textbf{Actividad 2: Simpson (videos 06--10)}}
\begin{itemize}
\item Estudien la deducción de la regla de Simpson, su ejemplo y el análisis del error.
\item Continúen con la deducción y el ejemplo de Simpson compuesto. Identifiquen la condición de que $n$ sea par y el patrón de los coeficientes.
\item Repitan los cálculos antes de consultar la solución. Distingan el error real de su cota y reconozcan el uso de la cuarta derivada.
\end{itemize}

\columnbreak
{\color{actividades}\textbf{Actividad 3: Cuadratura gaussiana (videos 11--15)}}
\begin{itemize}
\item Revisen el planteamiento de la cuadratura gaussiana y la elección de nodos y pesos.
\item Estudien Gauss-Legendre de dos puntos: deducción y ejemplos. Continúen con la deducción y el ejemplo de tres puntos.
\item Practiquen el cambio de variable de $[a,b]$ a $[-1,1]$, incluyendo el factor que multiplica la integral.
\item Revisen el resumen de dos, tres y cuatro puntos; identifiquen los nodos, pesos y grados de exactitud correspondientes.
\end{itemize}

{\color{actividades}\textbf{Actividad 4: Síntesis y preparación}}
\begin{itemize}
\item Elaboren un cuadro con cada regla, sus condiciones de aplicación y la información necesaria para estimar el error, cuando el material la incluya.
\item Comparen las aproximaciones de los ejemplos y registren las dudas que surjan.
\item Repasen interpolación y regresión para los quices presenciales de la semana 13.
\end{itemize}
El video 01, sobre rectángulo compuesto, queda como repaso opcional de lo ya estudiado.
\end{multicols}'''+s[b:]
s=s.replace('El estudiante deberá realizar todas las actividades antes de la o las clases sincrónicas según lo indique el docente.','Completen el recorrido de estudio de esta semana asincrónica y conserven sus cálculos para repasarlos y consultar sus dudas.')
(out/'main.tex').write_text(s,encoding='utf-8')

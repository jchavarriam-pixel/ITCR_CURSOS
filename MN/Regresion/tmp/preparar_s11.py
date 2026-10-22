from pathlib import Path
import shutil
out=Path('tmp/orientacion-s11'); src=Path('tmp/orientacion-s12')
for folder in ('imagenes','Direcciones'): shutil.copytree(src/folder,out/folder,dirs_exist_ok=True)
s=(src/'main.tex').read_text(encoding='utf-8').replace('Semana 12','Semana 11')
a=s.index('La clase de la \\textbf{semana 12')
b=s.index('{\\color{titulos}',a)
s=s[:a]+r'''Durante la \textbf{semana 11} se repasó la integral definida, su interpretación gráfica, el teorema fundamental del cálculo y la regla de Barrow. Se introdujeron las fórmulas de Newton-Cotes y se estudiaron la \textbf{regla del rectángulo simple y la regla del rectángulo compuesta}. Esta orientación organiza el repaso y la práctica de esos contenidos.

'''+s[b:]
a=s.index('{\\footnotesize\n\\textbf{Orden de estudio:}')
b=s.index('\\end{minipage}',a)
s=s[:a]+r'''{\footnotesize
\textbf{Recursos de estudio:}\\[0.2cm]
Notas de clase y libro de texto para el repaso de integración definida y la introducción a Newton-Cotes.\\[0.2cm]
\href{https://jchavarriam-pixel.github.io/ITCR_CURSOS/MN/IntegracionNumerica/#rectangulo-compuesto}{\textbf{Video 01 de la guía web:}} Regla compuesta del rectángulo.\\[0.2cm]
Intenten los cálculos antes de consultar el desarrollo escrito.
}
'''+s[b:]
a=s.index('\\textbf{Semana 13:}')
b=s.index('\\end{minipage}',a)
s=s[:a]+r'''\textbf{Práctica de la semana:}

Resuelvan los ejercicios de integral definida y de las reglas del rectángulo simple y compuesta indicados en esta orientación.

Conserven sus procedimientos y registren las dudas para consultarlas.
\vfill
'''+s[b:]
# Preserve verbatim the contents and objectives from the former week 11 orientation.
t=Path(r'C:\Users\jeffz\OneDrive\ITCR\2026\IIS26\Cursos\MN\Consignas IS26\Orientación S11 IS26\Orientacion_S11.tex').read_text(encoding='utf-8')
for heading in ('Contenidos:', 'Objetivos:'):
    pos=t.index(heading); start=t.index('{ \\tiny $\\blacksquare$}',pos); end=t.index('{\\color{white}\\rule',start)
    pos=s.index(heading); start2=s.index('{\\footnotesize',pos); end2=s.index('{\\color{white}\\rule',start2)
    s=s[:start2]+'{\\footnotesize\n'+t[start:end].strip()+'\n}\n\n'+s[end2:]
a=s.index('\\begin{multicols}{2}')
b=s.index('{ \\fboxsep 12pt',a)
s=s[:a]+r'''\begin{multicols}{2}
{\color{actividades}\textbf{Actividad 1: Integral definida}}
\begin{itemize}
\item Repasen la definición de integral definida y la partición de un intervalo. Consulten la sección 5.3 del libro, páginas 339--342.
\item Interpreten la integral como área con signo y distingan este valor del área geométrica total.
\item Repasen el teorema fundamental del cálculo y la regla de Barrow: si $F'=f$, entonces $\int_a^b f(x)\,dx=F(b)-F(a)$, bajo las hipótesis correspondientes.
\end{itemize}

{\color{actividades}\textbf{Actividad 2: Newton-Cotes y rectángulo}}
\begin{itemize}
\item Revisen la idea de las fórmulas de Newton-Cotes: aproximar la función mediante un polinomio interpolador e integrar ese polinomio.
\item Estudien la regla del rectángulo simple y su interpretación gráfica, según la convención utilizada en clase.
\item Estudien los ejemplos 123, 124 y 125 del libro relacionados con la regla del rectángulo.
\end{itemize}

\columnbreak
{\color{actividades}\textbf{Actividad 3: Rectángulo compuesto}}
\begin{itemize}
\item Construyan una partición uniforme con $n$ subintervalos y ancho $h=(b-a)/n$.
\item Identifiquen los puntos de evaluación utilizados en clase y sumen las contribuciones de los rectángulos.
\item Revisen el video 01 de la guía web y su desarrollo escrito. En este recurso se emplean extremos izquierdos.
\item Comparen el resultado con una integral de referencia y distingan el error real de una cota del error.
\end{itemize}

{\color{actividades}\textbf{Actividad 4: Ejercicios asignados}}
\begin{enumerate}
\item Para $f(x)=x^2$ en $[0,2]$, dibujen la región y calculen la integral definida mediante la regla de Barrow. Expliquen su relación con el área.
\item Para $f(x)=x-1$ en $[0,2]$, calculen la integral definida y el área geométrica total. Justifiquen por qué difieren.
\item Para $\int_0^2 x^2\,dx$, apliquen la regla del rectángulo simple con extremo izquierdo. Luego, apliquen la regla compuesta con extremos izquierdos para $n=4$ y $n=8$. Comparen los errores absolutos con el valor exacto.
\item Resuelvan el enunciado del video 01: aproximen $\int_1^2 \frac{\operatorname{sen}x}{x}\,dx$ con rectángulos izquierdos y determinen $n$ para garantizar un error absoluto menor que $10^{-5}$. Comparen después con la solución de la guía.
\end{enumerate}
\end{multicols}

'''+s[b:]
s=s.replace('Completen el recorrido de estudio de esta semana asincrónica','Completen las actividades de repaso de la semana 11')
(out/'main.tex').write_text(s,encoding='utf-8')

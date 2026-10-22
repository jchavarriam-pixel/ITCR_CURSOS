from pathlib import Path
p=Path('tmp/orientacion-s12/main.tex')
s=p.read_text(encoding='utf-8')
s=s.replace('los contenidos de las semanas 11 y 12:', 'los contenidos de esta semana:')
a=s.index('{\\color{titulos}\\Large\\textbf{Ejercicios asignados}}')
b=s.index('\\end{multicols}',a)+len('\\end{multicols}')
s=s[:a]+r'''{\color{titulos}\Large\textbf{Ejercicios asignados para la semana 12}}

Realicen los siguientes ejercicios como parte del trabajo de la semana 12. Los correspondientes a la regla del rectángulo sirven como repaso de lo ya estudiado.

\begin{multicols}{2}
{\color{actividades}\textbf{Libro de texto}}
\begin{itemize}
\item Página 350, lista de ejercicios 5.3: ejercicios \textbf{2, 3a, 3b, 4 y 5}.
\item Página 356, lista de ejercicios 5.4: ejercicios \textbf{1, 2b y 3b}.
\item Página 360, lista de ejercicios 5.5: ejercicios \textbf{1, 2 y 3}.
\item Página 371, lista de ejercicios 5.6: \textbf{todos los ejercicios}.
\end{itemize}

\columnbreak
{\color{actividades}\textbf{Folleto de prácticas}}
\begin{itemize}
\item Página 78: ejercicio \textbf{6.2.7 (partes 1, 3, 4 y 5)}.
\item Página 79: ejercicio \textbf{6.2.10 (partes 3, 4 y 5)}.
\item Página 80: ejercicio \textbf{6.2.16 (partes 1 y 2)}.
\item Página 83: ejercicio \textbf{6.2.21 (parte 2)}.
\item Página 84: ejercicio \textbf{6.2.22 (partes 1 y 2)}.
\item Página 85: ejercicio \textbf{6.2.23 (parte 1)}.
\end{itemize}
\end{multicols}'''+s[b:]
p.write_text(s,encoding='utf-8')

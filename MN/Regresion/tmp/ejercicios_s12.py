from pathlib import Path
p=Path('tmp/orientacion-s12/main.tex')
s=p.read_text(encoding='utf-8')
a=s.index('\\end{multicols}')+len('\\end{multicols}')
addition=r'''

\newpage
{\color{titulos}\Large\textbf{Ejercicios asignados}}

Realicen los ejercicios asignados en las orientaciones de las semanas 11 y 12. Los correspondientes a la regla del rectángulo sirven como repaso de lo ya estudiado.

\begin{multicols}{2}
{\color{actividades}\textbf{Semana 11}}

\textbf{Libro de texto}
\begin{itemize}
\item Página 350, lista de ejercicios 5.3: ejercicios \textbf{2, 3a, 3b, 4 y 5}.
\item Página 356, lista de ejercicios 5.4: ejercicios \textbf{1, 2b y 3b}.
\item Página 360, lista de ejercicios 5.5: ejercicios \textbf{1, 2 y 3}.
\end{itemize}

\textbf{Folleto de prácticas}
\begin{itemize}
\item Página 78: ejercicio \textbf{6.2.7 (parte 1)}.
\item Página 83: ejercicio \textbf{6.2.21 (parte 2)}.
\item Página 85: ejercicio \textbf{6.2.23 (parte 1)}.
\end{itemize}

\columnbreak
{\color{actividades}\textbf{Semana 12}}

\textbf{Libro de texto}
\begin{itemize}
\item Página 371, lista de ejercicios 5.6: \textbf{todos los ejercicios}.
\end{itemize}

\textbf{Folleto de prácticas}
\begin{itemize}
\item Página 78: ejercicio \textbf{6.2.7 (partes 3, 4 y 5)}.
\item Página 79: ejercicio \textbf{6.2.10 (partes 3, 4 y 5)}.
\item Página 80: ejercicio \textbf{6.2.16 (partes 1 y 2)}.
\item Página 84: ejercicio \textbf{6.2.22 (partes 1 y 2)}.
\end{itemize}
\end{multicols}
'''
s=s[:a]+addition+s[a:]
p.write_text(s,encoding='utf-8')

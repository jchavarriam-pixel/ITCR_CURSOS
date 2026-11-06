from pathlib import Path
import shutil
base=Path(r'C:\Users\jeffz\OneDrive\ITCR\2026\IIS26\Cursos\MN\Consignas IS26')
out=Path('tmp/orientacion-s13');out.mkdir(exist_ok=True)
for folder,source in [('imagenes',base/'Orientación S13 IS26/imagenes'),('Direcciones',base/'Direcciones')]:shutil.copytree(source,out/folder,dirs_exist_ok=True)
s=(base/'Orientación S13 IS26/Orientacion_S13.tex').read_text(encoding='utf-8')
s=s.replace('../Direcciones/','Direcciones/')
# Widen evaluations by borrowing space from the video column.
s=s.replace(r'\begin{minipage}[l][9.6cm]{3.9cm}',r'\begin{minipage}[l][9.6cm]{3.15cm}',1)
a=s.index('\\fcolorbox {cuadro3}')
pos=s.index(r'\begin{minipage}[l][9.6cm]{3.15cm}',a)
s=s[:pos]+s[pos:].replace(r'\begin{minipage}[l][9.6cm]{3.15cm}',r'\begin{minipage}[l][9.6cm]{3.9cm}',1)
a=s.index('\\footnotesize',s.index('{\\large Evaluación}'))
b=s.index('\\end{minipage}',a)
s=s[:a]+r'''\footnotesize\raggedright
\textbf{Clase presencial y quiz}\\
Mañana, \textbf{martes 27 de octubre}, la clase será presencial y se aplicará un quiz sobre \textbf{interpolación y regresión lineal}.

\medskip
\textbf{Tercer quiz virtual}\\
Esta semana se habilitará el tercer quiz virtual sobre \textbf{interpolación y regresión lineal}.

\medskip
\textbf{Defensas del laboratorio 1}\\
Se realizarán esta semana. Mañana, durante la clase, coordinaremos con los grupos las fechas y horarios.

\medskip
\textbf{Laboratorio 2}\\
Al finalizar la semana se asignará el segundo laboratorio, junto con las indicaciones para su desarrollo.
'''+s[b:]
(out/'main.tex').write_text(s,encoding='utf-8')

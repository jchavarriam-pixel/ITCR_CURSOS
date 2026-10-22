from pathlib import Path
p=Path('tmp/orientacion-s11/main.tex');s=p.read_text(encoding='utf-8')
a=s.index('{ \\fboxsep 12pt',s.index('Respuestas de la actividad 4'))
b=s.index('%{\\color{actividades}',a)
recap=s[a:b];s=s[:a]+s[b:]
pos=s.index('\\newpage\n{\\color{titulos}\\Large\\textbf{Respuestas')
s=s[:pos]+recap+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')

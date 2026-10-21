from pathlib import Path
base=Path(r'C:\Users\jeffz\OneDrive\ITCR\2026\IIS26\Cursos\MN\Consignas IS26')
p=Path('tmp/orientacion-s12/main.tex')
s=p.read_text(encoding='utf-8')
for heading in ('Contenidos:', 'Objetivos:'):
    parts=[]
    for week in (11,12):
        t=(base/f'Orientación S{week} IS26'/f'Orientacion_S{week}.tex').read_text(encoding='utf-8')
        a=t.index(heading)
        a=t.index('{ \\tiny $\\blacksquare$}',a)
        b=t.index('{\\color{white}\\rule',a)
        parts.append(t[a:b].strip())
    start=s.index(heading)
    a=s.index('{\\footnotesize',start)
    b=s.index('{\\color{white}\\rule',a)
    s=s[:a]+'{\\footnotesize\n'+ '\\\\[0.2cm]\n'.join(parts)+'\n}\n\n'+s[b:]
p.write_text(s,encoding='utf-8')

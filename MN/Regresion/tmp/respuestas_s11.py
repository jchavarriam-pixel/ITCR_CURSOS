from pathlib import Path
p=Path('tmp/orientacion-s11/main.tex')
s=p.read_text(encoding='utf-8')
s=s.replace('{\\color{actividades}\\textbf{Actividad 4: Ejercicios asignados}}',r'''{\color{actividades}\textbf{Actividad 4: Ejercicios de práctica}}

Los ejercicios 1--3 se elaboraron para esta orientación; el ejercicio 4 corresponde al video 01 de la guía web. Las respuestas se incluyen en la página siguiente.''')
a=s.index('\\end{multicols}')+len('\\end{multicols}')
s=s[:a]+r'''

\newpage
{\color{titulos}\Large\textbf{Respuestas de la actividad 4}}

Intenten resolver cada ejercicio antes de consultar estas respuestas. En las reglas del rectángulo se utilizan extremos izquierdos, tal como indican los enunciados.

{\color{actividades}\textbf{1. Integral de $x^2$ en $[0,2]$}}

Una primitiva es $F(x)=x^3/3$. Por la regla de Barrow,
\[
\int_0^2 x^2\,dx=\left[\frac{x^3}{3}\right]_0^2=\boxed{\frac83}.
\]
La región está entre la curva $y=x^2$, el eje horizontal y las rectas $x=0$ y $x=2$. Como $x^2\geq0$, la integral coincide con el área geométrica: $8/3$ unidades cuadradas.

{\color{actividades}\textbf{2. Integral de $x-1$ y área geométrica}}
\[
\int_0^2(x-1)\,dx=\left[\frac{x^2}{2}-x\right]_0^2=\boxed{0}.
\]
La función cambia de signo en $x=1$. Las dos regiones son triángulos de base y altura iguales a 1: cada uno tiene área $1/2$. La integral suma las áreas con signo, $-1/2+1/2=0$, mientras que el área geométrica total es $\boxed{1}$ unidad cuadrada.

{\color{actividades}\textbf{3. Rectángulos para $\int_0^2 x^2\,dx$}}

Con un solo rectángulo izquierdo, $R=(2-0)f(0)=\boxed{0}$. Para la regla compuesta,
\[
L_n=h\sum_{i=0}^{n-1}(ih)^2,\qquad h=\frac2n,
\qquad L_n=\frac{4(n-1)(2n-1)}{3n^2}.
\]
\begin{center}
\begin{tabular}{c|c|c|c}
Método & $h$ & Aproximación & Error absoluto $|8/3-L_n|$\\ \hline
Simple izquierdo & $2$ & $0$ & $8/3\approx2.666667$\\
Compuesto, $n=4$ & $1/2$ & $7/4=1.75$ & $11/12\approx0.916667$\\
Compuesto, $n=8$ & $1/4$ & $35/16=2.1875$ & $23/48\approx0.479167$
\end{tabular}
\end{center}
Las aproximaciones son menores que la integral porque $x^2$ es creciente y se usan extremos izquierdos. Al aumentar el número de rectángulos, el error disminuye.

{\color{actividades}\textbf{4. Rectángulo compuesto del video 01}}

Para $f(x)=\operatorname{sen}(x)/x$ en $[1,2]$, con ángulos en radianes, el desarrollo de la guía establece $|f'(x)|\leq M=0.4354$. La cota para rectángulos izquierdos da
\[
|I-L_n|\leq\frac{(b-a)^2M}{2n}=\frac{0.4354}{2n}.
\]
Para garantizar un error menor que $10^{-5}$ mediante esta cota, se exige $n>21770$; por tanto, el menor entero que satisface esta condición es $\boxed{n=21771}$. Entonces,
\[
L_{21771}=\frac1{21771}\sum_{i=0}^{21770}
\frac{\operatorname{sen}(1+i/21771)}{1+i/21771}
\approx\boxed{0.659338790}.
\]
La cota es aproximadamente $9.99954\times10^{-6}<10^{-5}$. Con $I\approx0.659329906$, el error real es aproximadamente $8.88\times10^{-6}$, y respeta la cota.

'''+s[a:]
p.write_text(s,encoding='utf-8')

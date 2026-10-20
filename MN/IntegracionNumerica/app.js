'use strict';
(() => {
 const C=window.Integracion,{m,esc,lessons,blocks}=C;
 const $=id=>document.getElementById(id);
 const storageKey='mn-integracion-numerica-v1';
 let state={seen:[],last:''},current=-1;
 try{const saved=JSON.parse(localStorage.getItem(storageKey)||'null');if(saved&&typeof saved==='object')state={seen:Array.isArray(saved.seen)?saved.seen.filter(id=>lessons.some(l=>l.id===id)):[],last:typeof saved.last==='string'?saved.last:'',notes:saved.notes};}catch{}
 const save=()=>{try{localStorage.setItem(storageKey,JSON.stringify(state));}catch{}};
 const video=l=>window.VIDEOS_INTEGRACION.find(v=>v.id===l.id)||{};
 const two=i=>String(i+1).padStart(2,'0');
 const d10=x=>Number.isFinite(x)?x.toFixed(10):'—';

 function renderMath(root=document){root.querySelectorAll('[data-math]').forEach(el=>{const tex=el.dataset.math.replaceAll('\\sum','\\displaystyle\\sum');try{katex.render(tex,el,{displayMode:el.dataset.display==='true',throwOnError:true,strict:'ignore',trust:false});}catch(e){el.classList.add('math-error');el.textContent=el.dataset.math;console.error('Fórmula no compuesta:',el.dataset.math,e.message);}});}

 /* ---------------------------------------------------------------- gráficas de exploración */
 const FUNCIONES=[
  {id:'senx',nombre:'sen(x)/x en [1, 2] (la integral de los ejemplos)',f:x=>Math.sin(x)/x,a:1,b:2},
  {id:'oscila',nombre:'2 + sen(3x) en [0, 4] (oscila)',f:x=>2+Math.sin(3*x),a:0,b:4},
  {id:'campana',nombre:'3·e^(−x²) en [−2, 2] (campana)',f:x=>3*Math.exp(-x*x),a:-2,b:2},
  {id:'cubica',nombre:'x³ − 3x + 3 en [−2, 2.5] (cambia de concavidad)',f:x=>x**3-3*x+3,a:-2,b:2.5},
  {id:'raiz',nombre:'√x en [0, 4] (pendiente infinita en 0)',f:x=>x>=0?Math.sqrt(x):NaN,a:0,b:4},
  {id:'pico',nombre:'1/(1 + 4x²) en [−3, 3] (pico estrecho)',f:x=>1/(1+4*x*x),a:-3,b:3},
  {id:'exponencial',nombre:'e^(x/2)·cos(2x) + 2 en [0, 5] (oscila y crece)',f:x=>Math.exp(x/2)*Math.cos(2*x)+2,a:0,b:5}
 ];
 const NODOS={2:[[-1/Math.sqrt(3),1],[1/Math.sqrt(3),1]],3:[[-Math.sqrt(.6),5/9],[0,8/9],[Math.sqrt(.6),5/9]],
  4:[[-0.8611363115940526,0.3478548451374538],[-0.3399810435848563,0.6521451548625461],[0.3399810435848563,0.6521451548625461],[0.8611363115940526,0.3478548451374538]]};
 const referencia=(f,a,b)=>{const n=20000,h=(b-a)/n;let s=f(a)+f(b);for(let i=1;i<n;i++)s+=(i%2?4:2)*f(a+i*h);return s*h/3;};
 const METODOS={
  rectangulo:{nombre:'Rectángulos (extremo izquierdo)',min:1,paso:1,aprox:(f,a,b,n)=>{const h=(b-a)/n;let s=0;for(let i=0;i<n;i++)s+=f(a+i*h);return h*s;}},
  trapecio:{nombre:'Trapecios',min:1,paso:1,aprox:(f,a,b,n)=>{const h=(b-a)/n;let s=(f(a)+f(b))/2;for(let i=1;i<n;i++)s+=f(a+i*h);return h*s;}},
  simpson:{nombre:'Parábolas de Simpson',min:2,paso:2,aprox:(f,a,b,n)=>{const h=(b-a)/n;let s=f(a)+f(b);for(let i=1;i<n;i++)s+=(i%2?4:2)*f(a+i*h);return h*s/3;}},
  gauss:{nombre:'Gauss-Legendre',aprox:(f,a,b,n)=>(b-a)/2*NODOS[n].reduce((s,[u,w])=>s+w*f((a+b)/2+(b-a)*u/2),0)}
 };
 const marcas=(lo,hi)=>{const r=hi-lo||1,base=10**Math.floor(Math.log10(r/4)),paso=[1,2,5,10].map(k=>k*base).find(p=>r/p<=6);const out=[];for(let v=Math.ceil(lo/paso)*paso;v<=hi+1e-9;v+=paso)out.push(Number(v.toPrecision(10)));return out;};
 const lagrange=(xs,ys)=>x=>xs.reduce((s,xi,i)=>s+ys[i]*xs.reduce((p,xj,j)=>j===i?p:p*(x-xj)/(xi-xj),1),0);

 function dibujar(svg,F,metodo,n){
  const {f,a,b}=F,W=800,H=360,ext=.15*(b-a),xs0=a-ext,xs1=b+ext;
  const muestra=Array.from({length:401},(_,i)=>xs0+(xs1-xs0)*i/400).map(x=>f(x)).filter(Number.isFinite);
  let yMin=Math.min(0,...muestra),yMax=Math.max(0,...muestra);const pad=.06*(yMax-yMin||1);yMax+=pad;if(yMin<0)yMin-=pad;
  const fr=EjesCartesianos({width:W,height:H,a,b,yMin,yMax,extend:.15,left:62,right:34,top:28,bottom:46,xTicks:marcas(Math.min(0,a),Math.max(0,b)),yTicks:marcas(yMin,yMax)}),{px,py}=fr;
  const camino=(g,x0,x1,pasos=200)=>{let out='',pluma='M';for(let i=0;i<=pasos;i++){const x=x0+(x1-x0)*i/pasos,y=g(x);if(!Number.isFinite(y)){pluma='M';continue;}out+=`${pluma}${px(x).toFixed(2)},${py(y).toFixed(2)} `;pluma='L';}return out;};
  const region=(g,x0,x1,color,op=.16,borde=true)=>`<path d="${camino(g,x0,x1,80)}L${px(x1)},${py(0)} L${px(x0)},${py(0)} Z" fill="${color}" fill-opacity="${op}" ${borde?`stroke="${color}" stroke-width="1.6"`:'stroke="none"'}/>`;
  let fig='',puntos=[];
  if(metodo==='rectangulo'||metodo==='trapecio'||metodo==='simpson'){
   const h=(b-a)/n;
   for(let i=0;i<n;i+=(metodo==='simpson'?2:1)){
    const x0=a+i*h;
    if(metodo==='rectangulo'){const y=f(x0);fig+=`<polygon points="${px(x0)},${py(0)} ${px(x0)},${py(y)} ${px(x0+h)},${py(y)} ${px(x0+h)},${py(0)}" fill="#315ad3" fill-opacity=".14" stroke="#315ad3" stroke-width="1.5"/>`;puntos.push(x0);}
    if(metodo==='trapecio'){fig+=`<polygon points="${px(x0)},${py(0)} ${px(x0)},${py(f(x0))} ${px(x0+h)},${py(f(x0+h))} ${px(x0+h)},${py(0)}" fill="#315ad3" fill-opacity=".14" stroke="#315ad3" stroke-width="1.5"/>`;}
    if(metodo==='simpson'){const q=lagrange([x0,x0+h,x0+2*h],[f(x0),f(x0+h),f(x0+2*h)]);fig+=region(q,x0,x0+2*h,['#315ad3','#8a4fc1'][(i/2)%2]);}
   }
   if(metodo!=='rectangulo')puntos=Array.from({length:n+1},(_,i)=>a+i*h);
  }else{
   const xs=NODOS[n].map(([u])=>(a+b)/2+(b-a)*u/2),q=lagrange(xs,xs.map(f));
   fig+=region(q,a,b,'#315ad3');fig+=`<path d="${camino(q,a,b)}" fill="none" stroke="#315ad3" stroke-width="2" stroke-dasharray="6 4"/>`;puntos=xs;
  }
  const guias=puntos.map(x=>{const y=f(x);return Number.isFinite(y)?`<line x1="${px(x)}" y1="${py(0)}" x2="${px(x)}" y2="${py(y)}" stroke="#91a4b9" stroke-dasharray="3 3"/><circle cx="${px(x)}" cy="${py(y)}" r="${n>24?2.5:4}" fill="#d79b25" stroke="white" stroke-width="1.2"/>`:'';}).join('');
  svg.innerHTML=`<defs><clipPath id="clip${svg.dataset.i}"><rect x="${fr.left}" y="${fr.top}" width="${W-fr.left-fr.right}" height="${H-fr.top-fr.bottom}"/></clipPath></defs>${fr.grid}<g clip-path="url(#clip${svg.dataset.i})">${region(f,a,b,'#007d79',.10,false)}${fig}<path d="${camino(f,fr.curveMin,fr.curveMax,400)}" fill="none" stroke="#007d79" stroke-width="2.8"/>${[a,b].map(x=>`<line x1="${px(x)}" y1="${fr.top}" x2="${px(x)}" y2="${H-fr.bottom}" stroke="#c45a3b" stroke-width="1.2" stroke-dasharray="2 5"/>`).join('')}${guias}</g>${fr.axes}`;
  renderMath(svg);
 }

 function iniciarGraficas(){
  document.querySelectorAll('[data-plot]').forEach((el,idx)=>{
   const [metodo,n0]=el.dataset.plot.split(':'),M=METODOS[metodo],gauss=metodo==='gauss';
   let n=Number(n0),F=FUNCIONES[0];
   const ctlN=gauss?`<label>Nodos <select data-n>${[2,3,4].map(k=>`<option value="${k}" ${k===n?'selected':''}>${k} puntos</option>`).join('')}</select></label>`:`<label>Subintervalos ${m('n')} <input type="range" data-n min="${M.min}" max="40" step="${M.paso}" value="${n}"> <output>${n}</output></label>`;
   el.innerHTML=`<figure class="plot-box"><div class="plot-toolbar"><label>Función <select data-f>${FUNCIONES.map((g,i)=>`<option value="${i}">${esc(g.nombre)}</option>`).join('')}</select></label>${ctlN}</div><svg viewBox="0 0 800 360" data-i="${idx}" role="img" aria-label="${esc(M.nombre)}"></svg><div class="legend"><span>Función</span><span>${esc(M.nombre)}</span><span>Puntos de evaluación</span></div><div class="plot-result"></div><figcaption>Cambia la función y ${gauss?'la cantidad de nodos':'la cantidad de subintervalos'} para ver qué figura construye el método y cómo cambia el error. La referencia es un cálculo numérico muy fino, no una antiderivada.</figcaption></figure>`;
   const svg=el.querySelector('svg'),res=el.querySelector('.plot-result'),out=el.querySelector('output');
   const actualizar=()=>{dibujar(svg,F,metodo,n);const q=M.aprox(F.f,F.a,F.b,n),I=referencia(F.f,F.a,F.b);res.innerHTML=`<span>Aproximación: <strong>${d10(q)}</strong></span><span>Integral (referencia): ${d10(I)}</span><span>Error absoluto: <strong>${d10(Math.abs(I-q))}</strong></span>`;};
   el.querySelector('[data-f]').addEventListener('change',e=>{F=FUNCIONES[Number(e.target.value)];actualizar();});
   el.querySelector('[data-n]').addEventListener('input',e=>{n=Number(e.target.value);if(out)out.value=n;actualizar();});
   actualizar();
  });
 }
 /* Gráfica que acompaña a cada video de explicación. */
 const GRAFICA={'rectangulo-compuesto':'rectangulo:4','trapecio-deduccion':'trapecio:1','trapecio-compuesto-deduccion':'trapecio:4','simpson-deduccion':'simpson:2',
  'simpson-error':'simpson:2','simpson-compuesto-deduccion':'simpson:6','cuadratura-gaussiana':'gauss:2','gauss-dos-puntos':'gauss:2','gauss-tres-puntos':'gauss:3','gauss-cuatro-puntos':'gauss:4'};

 /* ---------------------------------------------------------------- vistas */
 function updateNav(){
  $('temas').innerHTML=blocks.map((b,bi)=>`<h2>${esc(b.name)}</h2>${lessons.map((l,i)=>l.block===bi?`<a href="#${l.slug}" ${i===current?'class="active" aria-current="page"':''}><span class="nav-number">${two(i)}</span><span>${esc(l.title)}</span><span class="nav-check">${state.seen.includes(l.id)?'✓':''}</span></a>`:'').join('')}`).join('');
  $('progress').value=state.seen.length;$('progressText').textContent=`${state.seen.length} de ${lessons.length} videos vistos`;
 }
 function home(){return `<section class="hero solo"><div><span class="eyebrow">Métodos Numéricos · Guía de estudio</span><h1>Integración numérica</h1><p>Quince videos, en orden, con el procedimiento escrito de cada uno. En los ejercicios encontrarás primero el enunciado, después el video y debajo la solución completa tal como se desarrolla en la hoja del video.</p><a class="primary" href="#${lessons[0].slug}">Comenzar con el video 01 →</a>${state.last?` <a class="primary alt" href="#${esc(state.last)}">Continuar donde quedé →</a>`:''}<div class="meta-strip"><span>15 videos · 1 h 32 min</span><span>Enunciados y procedimientos escritos</span><span>Gráficas para explorar los métodos</span></div></div></section>
  <div class="grid3">${blocks.map((b,i)=>`<article class="chapter-card"><span class="chapter-n">${String(i+1).padStart(2,'0')}</span><h2>${b.name}</h2><p>${b.intro}</p><a href="#${lessons[b.first].slug}">${b.range} →</a></article>`).join('')}</div>
  <section class="section"><h2>Cómo estudiar con esta guía</h2><ol class="steps"><li><strong>Lee el enunciado</strong> e intenta plantear el problema antes de ver el video.</li><li><strong>Mira el video</strong> y pausa en cada paso para reproducirlo en tu cuaderno.</li><li><strong>Repasa el procedimiento escrito</strong> debajo del video: cada renglón lleva a la derecha su justificación, como en la hoja del video.</li><li><strong>Explora la gráfica</strong> en los videos de explicación: cambia la función y la partición para ver las figuras que construye cada método.</li></ol>${C.m?`<div class="callout">Las funciones trigonométricas se evalúan en <strong>radianes</strong>. Se usan diez decimales; se recomienda conservar todos los dígitos de la calculadora y redondear solo al final.</div>`:''}</section>
  <section class="section"><h2>Los quince videos</h2><ol class="route-list">${lessons.map((l,i)=>`<li><a href="#${l.slug}"><span class="nav-number">${two(i)}</span><span>${esc(l.title)} ${state.seen.includes(l.id)?'✓':''}</span><small>${esc(l.kind)} · ${esc(video(l).duracion||'')}</small></a></li>`).join('')}</ol></section>`;}
 function lesson(i){
  const l=lessons[i],v=video(l),ejercicio=Boolean(l.enunciado),graf=GRAFICA[l.slug];
  return `<header class="lesson-heading"><div class="lesson-meta"><span class="pill blue">${esc(blocks[l.block].name)}</span><span class="lesson-number">Video ${two(i)} de 15 · ${esc(l.kind)}${v.duracion?' · '+esc(v.duracion):''}</span></div><h1 tabindex="-1">${esc(l.title)}</h1><p>${esc(l.lead)}</p></header>
  ${ejercicio?`<section class="enunciado"><span class="eyebrow">Enunciado</span>${l.enunciado}</section>`:''}
  <div class="player" id="player"><button type="button" class="video-cover" id="playVideo"><span class="play-icon" aria-hidden="true">▶</span><strong>${esc(l.title)}</strong><small>Reproducir video ${two(i)}</small></button></div>
  <div class="video-problem" id="videoProblem" role="status" hidden></div>
  <div class="watch-actions"><a href="${esc(v.verEnDrive||window.CARPETA_VIDEOS_INTEGRACION)}" target="_blank" rel="noopener">Abrir video en Drive ↗</a><button type="button" id="markSeen" aria-pressed="${state.seen.includes(l.id)}">${state.seen.includes(l.id)?'✓ Video visto':'Marcar como visto'}</button></div>
  <article class="section lesson-body"><span class="eyebrow">${ejercicio?'Solución':'Desarrollo'}</span><h2>${ejercicio?'Procedimiento del video':'Desarrollo escrito del video'}</h2>${l.cuerpo()}</article>
  ${graf?`<section class="section"><span class="eyebrow">Explora</span><h2>Gráfica del método</h2><div data-plot="${graf}"></div></section>`:''}
  <nav class="lesson-bottom" aria-label="Navegación entre videos"><button type="button" id="previous"><small>${i===0?'Volver':'Video anterior'}</small>${i===0?'Inicio':'← '+esc(lessons[i-1].title)}</button><button type="button" id="next" class="primary"><small>${i===lessons.length-1?'Terminar':'Siguiente video'}</small>${i===lessons.length-1?'Volver al inicio ✓':esc(lessons[i+1].title)+' →'}</button></nav>`;
 }
 function setSeen(id,value){state.seen=state.seen.filter(x=>x!==id);if(value)state.seen.push(id);save();updateNav();if(current>=0&&lessons[current].id===id){$('markSeen').setAttribute('aria-pressed',String(value));$('markSeen').textContent=value?'✓ Video visto':'Marcar como visto';}}
 function startVideo(l){
  const config=video(l);
  if(!config.src){$('videoProblem').hidden=false;$('videoProblem').textContent='El video de esta lección todavía no tiene una dirección asignada.';return;}
  const player=$('player');player.replaceChildren();
  if(config.tipo==='iframe'){const frame=document.createElement('iframe');frame.title=`Video: ${l.title}`;frame.src=config.src;frame.allow='autoplay; encrypted-media; fullscreen; picture-in-picture';frame.allowFullscreen=true;frame.referrerPolicy='strict-origin-when-cross-origin';player.append(frame);}
  else{const vid=document.createElement('video');vid.controls=true;vid.preload='metadata';vid.playsInline=true;vid.src=config.src;vid.addEventListener('ended',()=>setSeen(l.id,true));player.append(vid);vid.play().catch(()=>{});}
 }
 function route(){
  const raw=decodeURIComponent(location.hash.slice(1)),hash=raw==='comparacion-y-cierre'?'gauss-cuatro-puntos':raw;
  current=lessons.findIndex(l=>l.slug===hash);
  $('vista').innerHTML=current<0?home():lesson(current);updateNav();renderMath($('vista'));
  document.body.classList.remove('menu-open');document.querySelector('.mobile-menu').setAttribute('aria-expanded','false');
  document.title=current<0?'Integración numérica · Métodos Numéricos':`${lessons[current].title} · Integración numérica`;
  if(current>=0){const l=lessons[current];state.last=l.slug;save();
   $('playVideo').onclick=()=>startVideo(l);$('markSeen').onclick=()=>setSeen(l.id,!state.seen.includes(l.id));
   $('previous').onclick=()=>location.hash=current===0?'inicio':lessons[current-1].slug;$('next').onclick=()=>location.hash=current===lessons.length-1?'inicio':lessons[current+1].slug;
   iniciarGraficas();}
  window.scrollTo({top:0,behavior:'instant'});
 }
 document.querySelector('.mobile-menu').onclick=()=>{const open=document.body.classList.toggle('menu-open');document.querySelector('.mobile-menu').setAttribute('aria-expanded',String(open));};
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){document.body.classList.remove('menu-open');document.querySelector('.mobile-menu').setAttribute('aria-expanded','false');}});
 $('resetProgress').onclick=()=>{state.seen=[];state.last='';save();updateNav();if(current>=0){$('markSeen').textContent='Marcar como visto';$('markSeen').setAttribute('aria-pressed','false');}};
 window.addEventListener('hashchange',route);
 window.IntegracionUI={renderMath};route();
})();

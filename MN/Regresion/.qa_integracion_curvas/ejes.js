'use strict';
/* Todas las gráficas del documento comparten un origen cartesiano real.
   El intervalo de integración y la ventana de visualización son independientes. */
window.EjesCartesianos=({width=800,height=340,a=1,b=2,yMin=0,yMax=1,left=65,right=35,top=28,bottom=48,color='#526b82',gridColor='#e1e7ed',labelColor='#53657a',fontSize=11,xTicks,yTicks,extend=.2}={})=>{
 const curveMin=a-extend*(b-a),curveMax=b+extend*(b-a);
 const xLo=Math.min(0,curveMin),xHi=Math.max(0,curveMax),yLo=Math.min(0,yMin),yHi=Math.max(0,yMax);
 const dx=Math.max(xHi-xLo,1e-9),dy=Math.max(yHi-yLo,1e-9);
 const xmin=xLo-.08*dx,xmax=xHi+.08*dx,ymin=yLo-.08*dy,ymax=yHi+.08*dy;
 const plotWidth=width-left-right,plotHeight=height-top-bottom;
 const px=x=>left+(x-xmin)/(xmax-xmin)*plotWidth,py=y=>height-bottom-(y-ymin)/(ymax-ymin)*plotHeight;
 const tickLo=Math.min(0,a),tickHi=Math.max(0,b),tx=xTicks||Array.from({length:5},(_,i)=>tickLo+(tickHi-tickLo)*i/4),ty=yTicks||Array.from({length:5},(_,i)=>yLo+(yHi-yLo)*i/4);
 const tex=v=>Number(v.toPrecision(7)).toLocaleString('es-CR',{maximumFractionDigits:9,useGrouping:false}).replace(',','{,}');
 const label=(s,x,y,w=54)=>`<foreignObject x="${x}" y="${y}" width="${w}" height="25"><div xmlns="http://www.w3.org/1999/xhtml" style="font-size:${fontSize}px;line-height:1.4;text-align:center;color:${labelColor}">${window.Integracion.m(s)}</div></foreignObject>`;
 const grid=tx.map(x=>`<line x1="${px(x)}" y1="${top}" x2="${px(x)}" y2="${height-bottom}" stroke="${gridColor}"/>`).join('')+ty.map(y=>`<line x1="${left}" y1="${py(y)}" x2="${width-right}" y2="${py(y)}" stroke="${gridColor}"/>`).join('');
 const axes=`<g data-cartesian-frame="true" data-x-zero="${px(0)}" data-y-zero="${py(0)}" data-x-min="${xmin}" data-x-max="${xmax}" data-y-min="${ymin}" data-y-max="${ymax}"><line data-axis="x" data-coordinate="0" x1="${left}" y1="${py(0)}" x2="${width-right}" y2="${py(0)}" stroke="${color}" stroke-width="1.7"/><line data-axis="y" data-coordinate="0" x1="${px(0)}" y1="${top}" x2="${px(0)}" y2="${height-bottom}" stroke="${color}" stroke-width="1.7"/>${tx.filter(v=>Math.abs(v)>1e-12).map(x=>label(tex(x),px(x)-27,py(0)+8)).join('')}${ty.filter(v=>Math.abs(v)>1e-12).map(y=>label(tex(y),px(0)-57,py(y)-10)).join('')}${label('0',px(0)-25,py(0)+7,25)}${label('x',width-right+3,py(0)-11,25)}${label('y',px(0)-12,Math.max(0,top-25),25)}</g>`;
 return {px,py,left,right,top,bottom,width,height,grid,axes,xmin,xmax,ymin,ymax,curveMin,curveMax};
};

import openpyxl,json,pathlib
w=openpyxl.load_workbook('Calificacion_revision.xlsx'); groups=[]
for s in list(w)[1:]:
 rows=[];section='';weight=0
 for r in range(1,s.max_row+1):
  a,b,c,d,e=[s.cell(r,j).value for j in range(1,6)]
  if isinstance(b,(int,float)) and isinstance(a,str) and '. ' in a: section=a;weight=b
  if isinstance(d,(int,float)) and c and section: rows.append({'row':r,'section':section,'weight':weight,'topic':c,'old':d,'reason':e})
 names=[s.cell(r,1).value for r in range(6,11) if s.cell(r,1).value not in ['Observación',None]]
 questions=[[s.cell(r,3).value,s.cell(r,5).value] for r in range(100,s.max_row+1) if isinstance(s.cell(r,1).value,str) and s.cell(r,1).value[:1].isdigit() and s.cell(r,3).value]
 groups.append({'name':s.title,'names':names,'rows':rows,'questions':questions})
pathlib.Path('audit/data.json').write_text(json.dumps(groups,ensure_ascii=False),encoding='utf8')

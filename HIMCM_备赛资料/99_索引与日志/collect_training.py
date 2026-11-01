#!/usr/bin/env python3
from collect_resources import *

cat='07_同级竞赛练习/M3官方题目与解答'
seeds=batch([
('https://m3challenge.siam.org/resources/sample-problems/',cat,'M3 sample problems','M3_练习总入口.html'),
('https://m3challenge.siam.org/resources/past-problems/',cat,'M3 past problems','M3_历年目录.html'),
('https://m3challenge.siam.org/resources/tips-and-guidance/','05_算法与代码文档/图表与写作','M3 tips and guidance','M3_建模与写作建议.html'),
('https://m3challenge.siam.org/resources/scoring-guide/','05_算法与代码文档/图表与写作','M3 scoring guide','M3_评审标准_仅供训练参考.html'),
])
pages=[]
for row in seeds[:2]:
    for u,t in links(row):
        if re.search(r'/past-problems/page/\d+/?$',u):pages.append((u,cat,'M3 historical index'))
rows=seeds[:2]+batch(dict((j[0],j) for j in pages).values())
years=[]
practice=[]
for row in rows:
    for u,t in links(row):
        if re.match(r'20\d{2} Problem:',t):
            year=t[:4]
            years.append((u,cat+'/'+year,t,safe(t)+'.html','M3 与 HiMCM 为不同竞赛，仅用作同级训练'))
        elif t.startswith('Practice Problem:'):
            practice.append((u,cat+'/专题练习',t,safe(t)+'.html'))
yearrows=batch(dict((j[0],j) for j in years+practice).values())
docs=[]
for row in yearrows:
    for u,t in links(row):
        if Path(unquote(urlparse(u).path)).suffix.lower() in ('.pdf','.xlsx','.xls','.csv','.zip','.docx','.tex'):
            docs.append((u,row['category'],t,None,'来自 M3 官方公开题目页；与 HiMCM 提交规则无关'))
batch(dict((j[0],j) for j in docs).values())

# Follow only the public teaching module entries linked by COMAP itself.
modules=fetch('https://www.comap.org/resources/free-resources/comap-mathematical-modeling-modules','04_教材与训练/COMAP教学模块')
entries=[]
for u,t in links(modules):
    if '/item/' in u and 'modeling-module' in u:
        entries.append((u,'04_教材与训练/COMAP教学模块',t,None,'公开介绍页面；全文若受登录限制则不获取'))
modrows=batch(dict((j[0],j) for j in entries).values())
moddocs=[]
for row in modrows:
    for u,t in links(row):
        if unquote(urlparse(u).path).lower().endswith('.pdf'):
            moddocs.append((u,row['category'],t))
batch(dict((j[0],j) for j in moddocs).values())
export()

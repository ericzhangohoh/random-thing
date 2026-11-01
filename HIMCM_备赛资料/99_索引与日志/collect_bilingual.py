#!/usr/bin/env python3
from collect_resources import *

base='https://skckenneth.github.io/teaching/mathematical-modeling-lecture-programme/'
category='04_教材与训练/中英双语建模讲义_KennethCheng'
root=fetch(base,category,'Kenneth Cheng Mathematical Modeling Lecture Library','课程目录.html','作者公开讲义；CC BY-NC-SA 4.0；非 COMAP 官方材料')
units=[];docs=[]
for u,t in links(root):
    if re.search(r'/(lecture|foundation|writing|competition|supplement)[^/]*/?$',u) and u.startswith(base) and u!=base:
        slug=urlparse(u).path.rstrip('/').rsplit('/',1)[-1]
        units.append((u,category+'/'+slug,t,'单元介绍.html','作者自编教学讲义，不代表竞赛规则或标准答案'))
    ext=Path(unquote(urlparse(u).path)).suffix.lower()
    if ext in ('.pdf','.csv','.zip','.json') and 'skckenneth.github.io' in u:
        docs.append((u,category+'/合集与数据',t))
unitrows=batch(dict((j[0],j) for j in units).values())
for row in unitrows:
    for u,t in links(row):
        if Path(unquote(urlparse(u).path)).suffix.lower() in ('.pdf','.csv','.zip','.json') and 'skckenneth.github.io' in u:
            docs.append((u,row['category'],t))
batch(dict((j[0],j) for j in docs).values())
batch([('https://ecoist-ste.github.io/personal-website/pdf/himcm_paper.pdf','03_论文与评审/作者公开论文/2020','2020 HiMCM B Team 10878','2020_B_10878_作者公开版.pdf','作者公开主页来源；获奖等级未核验')])
export()

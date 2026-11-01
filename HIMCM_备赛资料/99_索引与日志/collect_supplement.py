#!/usr/bin/env python3
"""Explicit, bounded supplemental sources for the HiMCM study archive."""
from collect_resources import *

jobs=[
('https://m3challenge.siam.org/wp-content/uploads/siam-guidebook-final-press.pdf','04_教材与训练/SIAM建模手册','Math Modeling: Getting Started and Getting Solutions','SIAM_2014_建模入门与求解.pdf'),
('https://m3challenge.siam.org/wp-content/uploads/siam-technical-guidebook-web.pdf','04_教材与训练/SIAM建模手册','Math Modeling: Computing and Communicating','SIAM_2018_计算与表达.pdf'),
('https://m3challenge.siam.org/wp-content/uploads/siam-cards-final-press.pdf','04_教材与训练/SIAM建模手册','Math Modeling Reference Cards','SIAM_建模速查卡.pdf'),
('https://www.comap.org/resources/free-resources/gaimme','04_教材与训练/GAIMME','GAIMME 官方下载页','GAIMME_官方入口.html'),
('https://www.comap.org/images/resources/free_resources/GAIMME_Report.pdf','04_教材与训练/GAIMME','GAIMME English report','GAIMME_英文官方公开版.pdf'),
('https://comap.org/membership/free-student-resources/item/gaimme-guidelines-for-assessment-and-instruction-in-mathematical-modeling-chinese-education','04_教材与训练/GAIMME','GAIMME 中文版官方入口','GAIMME_中文版入口.html','仅保存公开介绍；如需注册或登录则不自动访问受限内容'),
('https://www.comap.org/resources/free-resources/comap-mathematical-modeling-modules','04_教材与训练/COMAP教学模块','COMAP 免费教学模块目录','COMAP_教学模块目录.html'),
('https://allendowney.github.io/ModSimPy/','04_教材与训练/Python建模与仿真','Modeling and Simulation in Python','ModSimPy_目录.html'),
('https://greenteapress.com/wp/think-stats-2e/','04_教材与训练/概率统计','Think Stats author page','ThinkStats_作者主页.html'),
('https://greenteapress.com/thinkstats2/thinkstats2.pdf','04_教材与训练/概率统计','Think Stats 2e','ThinkStats_第二版.pdf'),
('https://greenteapress.com/wp/think-complexity-2e/','04_教材与训练/复杂系统与网络','Think Complexity author page','ThinkComplexity_作者主页.html'),
('https://greenteapress.com/complexity2/thinkcomplexity2.pdf','04_教材与训练/复杂系统与网络','Think Complexity 2e','ThinkComplexity_第二版.pdf'),
('https://web.stanford.edu/~boyd/cvxbook/','04_教材与训练/优化进阶','Convex Optimization author page','ConvexOptimization_作者主页.html'),
('https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf','04_教材与训练/优化进阶','Boyd and Vandenberghe Convex Optimization','Boyd_Convex_Optimization.pdf','大学程度进阶参考，按需查阅'),
('https://otexts.com/fpp3/','04_教材与训练/时间序列预测','Forecasting: Principles and Practice 3e','FPP3_目录.html'),
('https://www.theoj.org/joss-papers/joss.00097/10.21105.joss.00097.pdf','05_算法与代码文档/方法论文','Herman and Usher 2017 SALib','2017_SALib_敏感性分析.pdf'),
('https://web.stanford.edu/~boyd/papers/pdf/cvxpy_paper.pdf','05_算法与代码文档/方法论文','Diamond and Boyd 2016 CVXPY','2016_CVXPY_凸优化建模.pdf'),
('https://docs.scipy.org/doc/scipy/tutorial/optimize.html','05_算法与代码文档/SciPy','SciPy Optimization Tutorial','SciPy_优化教程.html'),
('https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html','05_算法与代码文档/SciPy','SciPy linprog','SciPy_线性规划.html'),
('https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html','05_算法与代码文档/SciPy','SciPy milp','SciPy_混合整数规划.html'),
('https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html','05_算法与代码文档/SciPy','SciPy solve_ivp','SciPy_微分方程.html'),
('https://networkx.org/documentation/stable/tutorial.html','05_算法与代码文档/网络与图论','NetworkX tutorial','NetworkX_入门.html'),
('https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html','05_算法与代码文档/网络与图论','NetworkX shortest paths','NetworkX_最短路径.html'),
('https://networkx.org/documentation/stable/reference/algorithms/flow.html','05_算法与代码文档/网络与图论','NetworkX network flows','NetworkX_网络流.html'),
('https://www.cvxpy.org/tutorial/intro/index.html','05_算法与代码文档/优化建模','CVXPY introduction','CVXPY_入门.html'),
('https://developers.google.com/optimization/routing/vrp','05_算法与代码文档/优化建模','OR-Tools vehicle routing','OR_Tools_车辆路径.html'),
('https://scikit-learn.org/stable/common_pitfalls.html','05_算法与代码文档/验证与敏感性','scikit-learn common pitfalls','sklearn_数据泄漏与常见错误.html'),
('https://scikit-learn.org/stable/modules/cross_validation.html','05_算法与代码文档/验证与敏感性','scikit-learn cross validation','sklearn_交叉验证.html'),
('https://salib.readthedocs.io/en/latest/user_guide/basics.html','05_算法与代码文档/验证与敏感性','SALib basics','SALib_全局敏感性分析.html'),
('https://simpy.readthedocs.io/en/latest/simpy_intro/index.html','05_算法与代码文档/仿真','SimPy intro','SimPy_离散事件仿真.html'),
('https://matplotlib.org/stable/tutorials/index.html','05_算法与代码文档/图表与写作','Matplotlib tutorials','Matplotlib_教程目录.html'),
('https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes','05_算法与代码文档/图表与写作','Overleaf LaTeX tutorial','LaTeX_入门.html'),
('https://data.worldbank.org/','06_数据来源导航','World Bank Open Data','世界银行_数据入口.html'),
('https://data.un.org/','06_数据来源导航','UNdata','联合国_数据入口.html'),
('https://ourworldindata.org/','06_数据来源导航','Our World in Data','OWID_数据入口.html'),
('https://www.abs.gov.au/statistics','06_数据来源导航','Australian Bureau of Statistics','澳大利亚统计局_数据入口.html'),
('https://www.data.gov.au/','06_数据来源导航','Australian Government Open Data','澳大利亚政府_数据入口.html'),
('https://data.stats.gov.cn/','06_数据来源导航','中国国家统计局国家数据','中国国家统计局_数据入口.html'),
('https://data.nasa.gov/','06_数据来源导航','NASA Open Data','NASA_数据入口.html'),
('https://www.ncei.noaa.gov/','06_数据来源导航','NOAA NCEI','NOAA_气候数据入口.html'),
('https://www.openstreetmap.org/','06_数据来源导航','OpenStreetMap','OpenStreetMap_地图入口.html'),
('https://www.comap.org/membership/mathmodels-members','03_论文与评审/官方会员入口','Mathmodels 官方论文与评审目录','Mathmodels_论文目录.html','目录公开；全文中部分需要会员，本归档不访问登录内容'),
('https://digitalcommons.imsa.edu/math_sw/','03_论文与评审/学校公开论文','IMSA Distinguished Student Work','IMSA_学校论文目录.html'),
('https://beldore.club/competitions/papers','03_论文与评审/公开镜像','Beldore public competition paper index','公开镜像_原始目录.html','第三方公开镜像；奖项标签需与 COMAP 原始结果交叉核验'),
]

batch(jobs)

# Only explicitly linked HiMCM and other high-school modeling papers; omit the
# undergraduate MCM/ICM collection already present in the user's folder.
row=RECORDS['https://beldore.club/competitions/papers']
papers=[]
for u,t in links(row):
    m=re.search(r'/competition-files/(himcm|immc)/(\d{4})/(.+\.pdf)$',u)
    if m:
        contest,year,tail=m.groups()
        cat=('03_论文与评审/HiMCM公开论文/' if contest=='himcm' else '07_同级竞赛练习/IMMC公开论文/')+year
        if '/' in tail:cat+='/'+safe(tail.rsplit('/',1)[0])
        papers.append((u,cat,t,Path(tail).name,'来源为第三方公开镜像；不等同于官方发布，未逐篇核验获奖等级'))
batch(papers)

# Archive the entire author-provided ModSimPy book as readable chapter snapshots.
row=RECORDS['https://allendowney.github.io/ModSimPy/']
chapters=[]
for u,t in links(row):
    if re.search(r'/ModSimPy/(?:chap\d+|preface)\.html$',u):
        chapters.append((u,'04_教材与训练/Python建模与仿真',t))
batch(dict((j[0],j) for j in chapters).values())

# IMSA links are openly offered by the school; access failures are logged.
row=RECORDS['https://digitalcommons.imsa.edu/math_sw/']
soup=BeautifulSoup((ROOT/row['local_path']).read_bytes(),'html.parser') if row['status']=='ok' else None
school=[]
if soup:
    for a in soup.select('a[href*="viewcontent.cgi"]'):
        u=urljoin(row['final_url'],a['href'])
        nxt=a.find_next('a')
        title=nxt.get_text(' ',strip=True) if nxt else 'IMSA paper'
        if not any(x in title for x in ['2015','2016','2017','Better Ate']):continue
        cat='03_论文与评审/学校公开论文' if 'HiMCM' in title or any(x in title for x in ['Go With','Safety','Hill Climbing','Lighting','Ski-Matic']) else '07_同级竞赛练习/M3学校论文'
        school.append((u,cat,title,safe(title)+'.pdf'))
batch(school)
export()

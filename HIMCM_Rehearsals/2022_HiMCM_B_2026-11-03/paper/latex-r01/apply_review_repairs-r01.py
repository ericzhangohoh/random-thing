from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parent
old=R/'manuscript-r02.tex';assert hashlib.sha256(old.read_bytes()).hexdigest()=='f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b'
s=old.read_text()
rep=[
('SUM02.04','We retain D as the prespecified selection without treating it as a universal future winner.','We retain D as the choice under the prespecified rule without treating it as a universal future winner.'),
('SUM04.03','The dates describe where a conditional annual curve crosses each level, rather than realized or sustained warming or Paris targets.','These are first crossing dates on a conditional annual curve, not dates of realized or sustained warming or Paris-target crossings.'),
('SUM06.01','Concentration and temperature are strongly associated at level, but the association weakens after trend removal and differencing.','Concentration and temperature are strongly associated in their observed levels, but the association weakens after trend removal and differencing.'),
('SUM05.02','A range based on earlier temperature errors misses the 2016 observation, and 2031 is merely the corresponding ten-year display cutoff from 2021.','A range based on earlier temperature errors misses the 2016 observation. Separately, 2031 is the display cutoff obtained by extending the tested ten-year horizon from 2021.'),
('VAL01.01','For development, each rule is fitted using observations available through 1981, 1986, 1991, 1996 and 2001, then predicts the following one to ten years.','For development, each rule is fitted to observations in the supplied workbook dated no later than 1981, 1986, 1991, 1996 or 2001, then predicts the following one to ten years from that origin.'),
('VAL03.03','The local computation preserves this order, but another reviewer had already exposed the final-period scores before the primary selection receipt.','The local computation preserves this order, but another reviewer had already exposed the final-period scores before the primary run recorded its selection.'),
('TEM03.01','At each origin, T1 is fitted to the observed concentration--temperature pairs available by that date.','At each origin, T1 is fitted to concentration--temperature pairs in the supplied workbook dated no later than that origin.'),
('TEM05.03','Calling T1-D the global minimum would therefore misrepresent the results.','T1-D is the selected sequential pipeline, while T1-Q is the lowest-error declared temperature comparator.'),
('FC05.02','The left panel includes the accepted log-concentration fit, while the right uses changes read from the accepted diagnostic series.','The left panel shows the fitted log-concentration relationship, while the right shows annual changes in log concentration and temperature anomaly.'),
('REL02.02',r'The contrast is visible in Figure~\ref{fig:association}.',r'Table~\ref{tab:association} gives the detrended comparisons, while Figure~\ref{fig:association} contrasts observed levels with annual changes.'),
('SEN02.04','They are not a new optimized model or probability bounds.','These results neither select a replacement model nor provide probability bounds.'),
('APP01.02','Each concentration model has few parameters, historical forecasts respect the observations available at their origin, and temperature scores include upstream concentration forecast error.','Each concentration model has few parameters, historical fits use only workbook observations dated no later than their origin, and temperature scores include upstream concentration forecast error.'),
('APP02.05','A logistic capacity is not identified by the rising record, and a physical carbon-cycle or energy-balance model would require inputs absent from the two supplied series.','The supplied record does not establish a physically justified saturation capacity, and a physical carbon-cycle or energy-balance model would require additional inputs absent from these two series.'),
('APP04.03','Already-above-origin and valid non-crossing-through-2300 cases receive different statuses.','Paths already above the threshold at the forecast origin are distinguished from valid paths that do not cross it by 2300.'),
('APP04.05','None of the actual primary paths requires such a rescue.','All actual primary paths remain valid throughout the search domain.'),
('ART05.04','They describe conditional annual paths, not established deadlines, sustained warming dates or Paris targets.','These are crossing dates on conditional annual paths, not established deadlines, sustained warming dates or Paris targets.')]
for id,a,b in rep:
 assert s.count(a)==1,(id,s.count(a));s=s.replace(a,b)
new=r'\p{DAT07}{These retrospective tests truncate one supplied data vintage by observation year. They do not reconstruct the data releases actually available at each historical forecast origin.}'
where=s.index('\n',s.index(r'\p{DAT02}'))
s=s[:where]+ '\n'+new+s[where:]
s=re.sub(r'(F0[1-6])-r01\.pdf',r'\1-r02.pdf',s)
p=R/'manuscript-r03.tex';assert not p.exists();p.write_text(s)
(R/'repair-instructions-r03.json').write_text(json.dumps({'source_from':str(old),'source_to':str(p),'replacements':[{'old_id':id,'old_tex':a,'new_tex':b} for id,a,b in rep],'added_block':new,'non_prose_change':'F05 legend Accepted log-CO2 fit -> Fitted log-CO2 curve. Other figure contents unchanged, new versioned outputs.'},indent=2)+'\n')
fig=R.parent.parent/'code/visualization/latex-r01/render_figures-r01.py';fs=fig.read_text().replace("{id}-r01.","{id}-r02.").replace('figure-register-r01.json','figure-register-r02.json').replace('Accepted log-CO2 fit','Fitted log-CO2 curve')
newfig=fig.with_name('render_figures-r02.py');assert not newfig.exists();newfig.write_text(fs)
print('Created source r03 and figure renderer r02, 16 old-record replacements and new DAT07 block.')

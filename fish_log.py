#!/usr/bin/env python
import os
from datetime import timedelta as timedelta
from datetime import datetime

os.chdir('/Users/josephwhalen/.fish_log/') #your home directory
num_days = 25 # number of days to chart, 25 fits on one page @ 17pt
start_date = datetime.now()
date_format = '%a %m/%d'
tex_file = './fish_log.tex'
printer = 'Lab_Printer' # the printer you want to print from

tex_header = r"""\documentclass[17pt,letterpaper]{extarticle}
\usepackage[margin=1in]{geometry}
\pagenumbering{gobble}
\usepackage{fancyhdr}
\pagestyle{fancy}
\usepackage{array}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\chead{One pinch of tetra-fin (orange can) twice daily}
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
\begin{center}
\begin{tabular}{|C{0.3\textwidth} |C{0.3\textwidth}|C{0.3\textwidth}|}
\hline
Date & AM & PM \\
\hline
"""

table_line = r'%s & & \\ \hline'+'\n'

tex_footer = r"""\end{tabular}
\end{center}
\end{document}"""

f = open(tex_file,'w')

f.write(tex_header)

for i in range(num_days):
    f.write(table_line % start_date.strftime(date_format))
    start_date += timedelta(days=1)

f.write(tex_footer)
f.close()

os.system('pdflatex '+tex_file+' > /dev/null')
os.system('rm *.aux')
os.system('rm *.log')
os.system('rm *.tex')

os.system('lp -d '+printer+' '+tex_file[:-4]+'.pdf') 

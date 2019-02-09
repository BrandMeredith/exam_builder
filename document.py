import sys
import os.path

class Document:
    '''Either an exam or a practice test.'''
    def __init__(self,problem_list):
        self.problem_list = list(problem_list) #copy list
        self.filename = os.getcwd()+'/exam.tex'
        self.title = "Exam"

    def generate_exam(self):
      file=open(self.filename,'w')

      # print basic stuff
      file.write('\documentclass[a4paper,12pt]{article}\n')
      file.write('\usepackage{amsmath}\n')
      file.write('\usepackage{amsthm}\n')
      file.write('\usepackage{amssymb}\n')
      file.write('\usepackage{multicol}\n')
      file.write('\usepackage{tikz}\n')
      file.write(r'\renewcommand{\labelenumi}{(\alph{enumi})}'+'\n')
      file.write(r'\newcommand{\lis}[1]{\begin{enumerate}#1\end{enumerate}}'+'\n')
      file.write(r'\newcommand{\pr}[1]{\stepcounter{probnum} \noindent \theprobnum. #1}'+'\n')
      file.write(r'\newcounter{probnum}'+'\n')
      file.write('\\begin{document}\n')

      # create title page
      file.write('\n')
      file.write('\\begin{center} \large{'+ self.title +'} \end{center}\n')
      file.write('\n')

      # print each problem
      for problem in self.problem_list:
        file.write('% Chapter: '+str(problem.chapter)+
          '  Section: '+str(problem.section)+
          '  Type: '+str(problem.type)+
          '  Difficulty: '+str(problem.difficulty)+'\n\n')
        file.write(r'\pr{')
        for line in problem.problem_text:
          file.write(line)
        file.write('}\\newpage\n\n\n')
      file.write('\\end{document}\n')

      return
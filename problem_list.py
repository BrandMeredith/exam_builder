import sys
import os.path
from problem import Problem

class Problem_list:
    '''Either an exam or a practice test.'''
    def __init__(self):
        self.list = self.file_to_list()
        self.chapter_section_list = self.create_chapter_section_list()

    def create_chapter_section_list(self):
        chapter_sections = []
        for problem in self.list:
            chapter_sections += [float(str(problem.chapter)+'.'+str(problem.section))]
        if 0 in chapter_sections:
            chapter_sections.remove(0)
        # return a sorted list with no repeats
        return sorted(list(set(chapter_sections)))

    def file_to_list(self):
        file = self.scan_for_input_file()
        text_chunks = self.text_to_chunks(file)
        problem_list = self.chunks_to_problem_list(text_chunks)
        return problem_list

    def scan_for_input_file(self):
      #scan the current working directory for a formatted question file. choose the first found, if any.
      for filename in os.listdir('.'): #loop over files in cwd - current working directory
        if 'txt' == filename.split('.')[1]: #accept files with extension txt
          file = open(filename,'r')
          for line in file:
              if len(line.split('@'))==5: #search for data tag lines
                return file
      return os.getcwd() #if no files found, input file starts as cwd stem

    @staticmethod
    def text_to_chunks(file):
      # break up text in file into chunks of text (creating a list of lists), each chunk giving the raw problem text
      text_chunks = []
      raw_problem_text = []
      for line in file:
        if line[0]==r'@':
          text_chunks += [raw_problem_text]
          raw_problem_text = [line]
        else:
          raw_problem_text += [line]
      return text_chunks[1:] #discard first chunk

    @staticmethod
    def chunks_to_problem_list(text_chunks):
        problem_list = []
        for chunk in text_chunks:
            chunk = list(chunk)
            problem_list += [Problem(chunk)]
        return problem_list
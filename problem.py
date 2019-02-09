import sys

class Problem:
    '''Either an exam or a practice test.'''
    def __init__(self,text):
        self.raw_text = list(text)
        [self.chapter,
            self.section,
            self.type,
            self.difficulty] = self.first_line_to_data(self.raw_text)
        self.problem_text = self.raw_text[1:] #all but the first line
        self.chapter_section = float(str(self.chapter)+'.'+str(self.section))

    @staticmethod
    def first_line_to_data(text):
        #split data tag lines over the special character into a list
        if len(text[0].split(r'@'))>1:
            [chapter, section, type, difficulty] = text[0].split(r'@')[1:] 
            return [chapter, section, type, difficulty]
        else:
            return [0,0,0,0]
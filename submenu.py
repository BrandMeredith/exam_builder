import sys

class Submenu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self,menu):
        self.sections = list(menu.full_problem_list.chapter_section_list) #copy list
        self.uncovered_sections = list(menu.uncovered_sections) #copy list
        self.covered_sections = list(menu.covered_sections) #copy list

    def display_menu(self):
      print 'Enter section. 0 to quit.'
      print '\n\033[4m'+'Sections'+'\033[0m'+'      '+'\033[4m'+'Coverage'+'\033[0m' #funny control sequence is underline
      for section in self.sections:
        if float(section) in self.covered_sections: 
            print '                 '+str(section) #gap to right column: 17 spaces
        else: 
            print '   '+str(section) #gap to left column: 3 spaces

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ")
            if choice == '0':
                break
            try:
                if float(choice) in self.sections:
                    self.swap(choice)
                else:
                    print str(choice)+' is invalid. Try again.'
            except:
                print str(choice)+' is invalid. Try again.'

    def swap(self,choice):
        choice_float = float(choice)
        if choice_float in self.covered_sections:
            self.covered_sections.remove(choice_float)
            self.uncovered_sections.append(choice_float)
        elif choice_float in self.uncovered_sections:
            self.covered_sections.append(choice_float)
            self.uncovered_sections.remove(choice_float)
        self.update_sections()

    def update_sections(self):
        self.sections = sorted(list(set(self.sections)))
        self.uncovered_sections = sorted(list(set(self.uncovered_sections)))
        self.covered_sections = sorted(list(set(self.covered_sections)))
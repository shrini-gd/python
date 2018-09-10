import operator

class School(object):
    def __init__(self):
       self.students = {}

    def add_student(self, name, grade):
       self.students[name] = grade 

    def roster(self):
       return [name for name, _ in sorted(self.students.items(), key=operator.itemgetter(1,0))]

    def grade(self, grade_number):
       return sorted([name for (name, grade) in self.students.items() if grade == grade_number])

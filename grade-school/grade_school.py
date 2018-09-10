from sortedcontainers import SortedDict, SortedList

class School(object):
    def __init__(self):
       self.students = SortedDict()

    def add_student(self, name, grade):
       if grade not in self.students.keys():
          self.students[grade] = SortedList()
       self.students[grade].add(name)

    def roster(self):
       return [name for names in self.students.values() for name in names]

    def grade(self, grade_number):
       if not self.students:
          return []
       return list(self.students[grade_number])

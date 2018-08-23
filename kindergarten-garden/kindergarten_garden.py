from collections import defaultdict
class Garden(object):
    plant_names = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}
    default_students = ['Alice','Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    def __init__(self, diagram, students=None):
       sorted_students = sorted(students or self.default_students) 
       input_diagram = diagram.split('\n')
       self.garden = defaultdict(list)	
       for i, student in enumerate(sorted_students):
          filtered_diagram = input_diagram[0][i*2:i*2+2]+input_diagram[1][i*2:i*2+2]
          for c in filtered_diagram:
             self.garden[student].append(self.plant_names[c])

    def plants(self, student):
         return self.garden[student]

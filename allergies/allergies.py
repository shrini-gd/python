class Allergies(object):

    allergy_score_chart = { 'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128 }
    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.allergy_score_chart[item] & self.score > 0 

    @property
    def lst(self):
       allergies = []	
       for k, v in self.allergy_score_chart.items():
          if self.is_allergic_to(k): 
             allergies.append(k)
       return allergies

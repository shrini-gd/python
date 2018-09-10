def saddle_points(matrix):
   for m in matrix:
      if len(m) != len(matrix):
        raise ValueError('invalid!')
   sp=set()
   transpose = [list(x) for x in zip(*matrix)]
   min_vals = [min(l) for l in transpose]
   for i, mt in enumerate(transpose):
      for j, m in enumerate(matrix): 
         if max(m) == min(mt):
            sp.add((j, i))
   return sp

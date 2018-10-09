def append(xs, ys):
   return xs + ys

def concat(lists):
   res=[]
   for lst in lists:
      res += lst
   return res

def filter_clone(function, xs):
   return [x for x in xs if function(x)] 

def length(xs):
   ln = 0
   for x in xs:
      ln += 1
   return ln

def map_clone(function, xs):
   return [function(x) for x in xs] 

def foldl(function, xs, acc):
   for x in xs:
      acc = function(acc, x)
   return acc

def foldr(function, xs, acc):
   for x in xs[::-1]:
      acc = function(x, acc)
   return acc

def reverse(xs):
   return xs[::-1]

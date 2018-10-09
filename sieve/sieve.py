# Reference: https://www.wikiwand.com/en/Sieve_of_Eratosthenes

import math
def sieve(limit):
   list = [True]*(limit+1)
   list[0] = False 
   list[1] = False
   for i in range(2, int(math.sqrt(limit))+1):
     if list[i] == True: 
       k = 1
       for j in range(i*i, limit+1, i*k):
         k += 1
         list[j] = False
   output = []
   for i, prime in enumerate(list):
      if prime:
        output.append(i)
   return output

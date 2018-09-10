def binary_search(numbers, number):
   start = 0 
   end = len(numbers) - 1
   while start <= end: 
     mid = (start + end) // 2 
     value = numbers[mid]
     if value < number:
       start = mid + 1
     elif value > number:
       end = mid - 1
     else:
       return mid
   raise ValueError('Number does not exist')

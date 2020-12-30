def doubler(numbers):
  number = []
  for item in numbers:
    item *= 2
    number.append(item)
    
  return number
  
print(doubler([1,2,3,4]))
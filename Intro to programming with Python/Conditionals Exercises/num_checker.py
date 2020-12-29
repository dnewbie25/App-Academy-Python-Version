def number_check(num):
  if num > 0:
    return 'positive'
  elif num < 0:
    return 'negative'
  else: 
    return 'zero'
  
print(number_check(3))
print(number_check(-3))
print(number_check(0))
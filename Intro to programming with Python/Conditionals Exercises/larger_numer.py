def larger_number(num1, num2):
  if num1 > num2:
    return num1
  elif num2 > num1:
    return num2
  else:
    return "They are the same"
  
print(larger_number(3,5))
print(larger_number(-9.8, 3.5))
print(larger_number(8,8))
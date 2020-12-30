def factorial(num):
  counter = 1
  product = 1
  while counter <= num:
    product *= counter
    counter += 1
    
  return product

print(factorial(10))
print(factorial(4))
def sum_nums(max):
  counter = 1
  sum = 0
  while counter <= max:
    sum += counter
    counter += 1
  
  return sum

print(sum_nums(50))
print(sum_nums(100))
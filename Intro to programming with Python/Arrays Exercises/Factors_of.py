def factors_of(num):
  counter = 1
  newarr = []
  while counter <= num:
    if num % counter == 0:
      newarr.append(counter)
    counter += 1

  return newarr

print(factors_of(3))
print(factors_of(4))
print(factors_of(16))
print(factors_of(31))
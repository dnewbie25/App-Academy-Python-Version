def fizz_buzz(max):
  newarr = []
  counter = 0
  while counter < max:
    if (counter%4 == 0 or counter%6==0) and not(counter%4 == 0 and counter%6==0):
      newarr.append(counter)
    counter += 1

  return newarr

print(fizz_buzz(20))
print(fizz_buzz(15))
print(fizz_buzz(16))
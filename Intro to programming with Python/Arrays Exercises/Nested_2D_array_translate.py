def array_translate(array):
  newarr = []
  count = 0
  while count < len(array)-1:
    newarr.append(array[count] * array[count+1])
    count += 2
  
  return ''.join(newarr) # this is how to join arrays

print(array_translate(["Cat", 2, "Dog", 3, "Mouse", 1]))
print(array_translate(["red", 3, "blue", 1]))

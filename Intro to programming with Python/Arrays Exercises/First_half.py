def first_half(array):
  newarr = []
  if len(array) % 2 == 0:
    half = len(array)/2
    counter = 0
    while counter < half:
      newarr.append(array[counter])
      counter += 1

  else:
    half = len(array)/2
    counter = 0
    while counter < half:
      newarr.append(array[counter])
      counter += 1

  return newarr

print(first_half(["Brian", "Abby", "David", "Ommi"]))
print(first_half(["a", "b", "c", "d", "e"]))
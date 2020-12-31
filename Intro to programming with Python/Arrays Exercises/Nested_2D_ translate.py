def two_d_translate(array):
  newarr = []
  for arr in array:
    count = arr[1]
    while count > 0:
      newarr.append(arr[0])
      count -= 1

  return newarr

print(two_d_translate([
  ['boot', 3],
  ['camp', 2],
  ['program', 0]
]))
print(two_d_translate([
  ['red', 1],
  ['blue', 4]
]))

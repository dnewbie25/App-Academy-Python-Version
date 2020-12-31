def opposite_count(array):
  opposites = 0
  count = 0
  for item in array:
    index = count
    while index < len(array):
      if item + array[index] == 0:
        opposites += 1
      index += 1
    count += 1

  return opposites

print(opposite_count([ 2, 5, 11, -5, -2, 7 ]))
print(opposite_count([ 21, -23, 24 -12, 23 ]))
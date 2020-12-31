def two_d_sum(array):
  sum = 0
  for arr1 in array:
    for arr2 in arr1:
      sum += arr2

  return sum

print(two_d_sum([
  [4, 5],
  [1, 3, 7, 1]
]))
print(two_d_sum([
  [3, 3],
  [2],
  [2, 5]
]))
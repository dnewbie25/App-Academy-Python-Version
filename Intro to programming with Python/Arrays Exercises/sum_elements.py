def sum_elements(arr1, arr2):
  index = 0
  newarr = []
  while index < len(arr1):
    newarr.append(arr1[index] + arr2[index])
    index += 1
  
  return newarr

print(sum_elements([7, 4, 4], [3, 2, 11]))
print(sum_elements(["cat", "pizza", "boot"], ["dog", "pie", "camp"]))
def combinations(arr):
  newarr = []
  counter = 0
  for item in arr:
    index = counter
    while index < len(arr):
      if counter != index:
        newarr.append([item, arr[index]])
      index += 1
    counter += 1

  return newarr

print(combinations([0, 1, 2, 3]))
print(combinations(["a", "b", "c"]))
def reverse_range(min, max):
  newarr = []
  max = max-1
  while max > min:
    newarr.append(max)
    max -= 1

  return newarr

print(reverse_range(10, 17))
print(reverse_range(1, 7))
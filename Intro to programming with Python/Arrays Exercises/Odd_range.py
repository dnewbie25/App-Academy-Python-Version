def odd_range(min, max):
  newarr = []
  while min <= max:
    if min % 2 != 0:
      newarr.append(min)
    min+=1
  return newarr
  
print(odd_range(11, 28))
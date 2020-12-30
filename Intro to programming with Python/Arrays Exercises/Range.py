def range(min, max):
  newarr = []
  while min <= max:
    newarr.append(min)
    min += 1
    
  return newarr
  
  
print(range(13, 20))
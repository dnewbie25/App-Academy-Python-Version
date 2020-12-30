def even_nums(max):
  newarr = []
  
  start = 0
  
  while start <= max:
    if start % 2 == 0:
      newarr.append(start)
    start += 1
    
  return newarr
  
print(even_nums(10))
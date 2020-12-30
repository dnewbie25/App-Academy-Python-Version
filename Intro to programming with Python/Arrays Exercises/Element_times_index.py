def element_times_index(nums):
  index = 0
  newarr = []
  while index < len(nums):
    newarr.append(nums[index]*index)
    index += 1
  
  return newarr

print(element_times_index([4,7,6,5]))
'''
puts either_only(9)  # => true
puts either_only(20) # => true
puts either_only(7)  # => false
puts either_only(15) # => false
puts either_only(30) # => false
'''

def either_only(num):
  if (num % 3 == 0 or num % 5 == 0) and not(num % 3 == 0 and num % 5 == 0):
    return True
  else:
    return False
  
print(either_only(9) ) # => true
print(either_only(20)) # => true
print(either_only(7)  )# => false
print(either_only(15) )# => false
print(either_only(30) )# => false
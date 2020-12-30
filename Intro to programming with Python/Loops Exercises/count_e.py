def count_e(word):
  e = 0
  for char in word:
    if char == 'e':
      e+=1
      
  return e

print(count_e('february'))
print(count_e('epenfede'))
print(count_e('edae'))
i = 0

while i <= 10:
  print(i)
  i += 1
print('Done!!')
print('******************************************\n')

for char in 'Python is the best':
  print(char * 10)
print('******************************************\n')  

for item in [1,2,3,4]:
  print(item * item)
print('******************************************\n')

for i in range(1,10): #inclusive-exclusive
  print(i)
print('******************************************\n')
  
for i in range(0,101,2): #inclusive, exclusive, step (adds 2 to each i)
  print(i)
print('******************************************\n')
  
#NESTED LOOPS

for x in range(4): # 0 to 3 inclusive
  for y in range(3): # 0 to 2 inclusive
    print(f"{x}, {y}")
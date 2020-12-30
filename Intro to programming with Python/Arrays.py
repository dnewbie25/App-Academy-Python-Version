# Called Lists
names = ['John', 'Maria', 'Sarah', 'David', 'Leonard', 'Stephen']

print(names[0])
print(names[:3]) # [0, 3)
print(names[2:]) # from index 2, Srah, to the end
print(names[2:6]) # [2, 6), that's why it works, inclusive-exclusive
print(names[2:6]) #Sarah, David, it is inclusive-exclusive [2, 4)
print(names[1:-2]) # ['Maria', 'Sarah', 'David']
print(names[:]) #prints all

# Some list methods

numbers = [1,2,3,4,5,6,7,8,0,7,7]

numbers.append(10) # adds at the end
print(numbers)
numbers.insert(3, 3.5) # adds the value 4.5 at index 3 [1,2,3,3.5,4]
print(numbers.pop()) #removes and return the last element, in this case the 10 we added before

print(numbers.index(5)) #return the element at index 5, in this case 5 because we added 3.5 before at idnex 3, so the rest of elements were moved to the right

print(5 in numbers) #True if it finds the element

print(numbers.count(7)) # the seven is repeated 3 times

numbers.sort() # sorts
print(numbers) 

numbers.reverse() #sorted backwards
print(numbers)

numbers2 = numbers.copy() # copy the entire list, this time it wil copy the list reversed because it was the last modification to it

numbers.append(50)
print(numbers)
print(numbers2) # doesn't returns the 50 as the last element because the copy was made before appending 50

unique_nums = []

for item in numbers:
  if item not in unique_nums:
    unique_nums.append(item) # adds the element if it's not in unique_nums

unique_nums.sort()
print(unique_nums)

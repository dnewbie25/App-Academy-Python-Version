course = 'Python for Beginners'

print(len(course)) # length
print(course.upper()) # uppercase: PYTHON
print(course.lower()) # lowercase: python
print(course.capitalize()) # capitalize: Python for beginners, first letter of the string is capital
print(course.title()) # title: Python For Beginners - first letter of each word is capital
print(course.find('for')) # 7, the index where 'for' appears
print(course.find('forest')) # -1 because it was not found
print(course.replace('Beginners', 'Absolute Beginners')) # Python for Absolute Beginners

print('python' in course) # false, boolean if it found the exact value

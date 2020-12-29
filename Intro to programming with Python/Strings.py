print('Strings Exercises!!')
word = "This-is-the-word"
print('Hello world!!' + '1234')
print(str(1234) + '1234')
print('Hello,\nHope\nYour\'re\n\t\tdoing\n\t\t\twell')
print(word[1:7]) # the same as word[1...7] in Ruby (inclusive-exclusive)

iseven = 10 % 2 == 0

print(iseven)

# Formatted strings

firstName = 'Daniel'
lastName = 'Montoya'

fullName = firstName + ' ' + lastName
fullName2 = f"{firstName} {lastName}"

print(fullName)
print(fullName2)
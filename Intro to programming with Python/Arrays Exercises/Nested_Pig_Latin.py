def pig_latin_word(word):
  vowels = 'aeiou'
  if word[0] in vowels:
    return word + 'yay'

  counter = 0
  while counter < len(word):
    if word[counter] in vowels:
      return word[counter:len(word)] + word[0:counter] + 'ay'
    counter += 1

print(pig_latin_word("apple") )  # => "appleyay"
print(pig_latin_word("eat")   )  # => "eatyay"
print(pig_latin_word("banana"))  # => "ananabay"
print(pig_latin_word("trash") )
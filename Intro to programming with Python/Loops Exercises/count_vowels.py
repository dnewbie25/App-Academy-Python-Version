def count_vowels(word):
  vowels = 'aeiou'
  count = 0
  for char in word:
    for vowel in vowels:
      if char == vowel:
        count += 1
  
  return count

print(count_vowels("bootcamp"))  # => 3
print(count_vowels("apple")   )  # => 2
print(count_vowels("pizza")   )  # => 2
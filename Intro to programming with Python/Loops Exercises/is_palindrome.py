import reverse # I imported a previous function y created
def is_palindrome(word):
  reverse_word = reverse.reverse(word)
  
  if reverse_word == word:
    return True
  else:
    return False
  
print(is_palindrome('anitalavalatina'))
print(is_palindrome('hello'))
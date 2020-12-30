def reverse(word):
  counter = len(word) - 1
  reversed_word = ''
  while counter >= 0:
    reversed_word += word[counter]
    counter -= 1
    
  return reversed_word

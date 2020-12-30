def yell(words):
  yelled_words = []
  for word in words:
    word += '!'
    yelled_words.append(word)
    
  return yelled_words

print(yell(['hello', 'how', 'are', 'you']))
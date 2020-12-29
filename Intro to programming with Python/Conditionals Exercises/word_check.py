def word_check(word):
  if len(word) > 6:
    return "long"
  elif len(word) < 6:
    return "short"
  else:
    return "medium"
  
print(word_check('mammamia'))
print(word_check('hi'))
print(word_check('perfos'))
  
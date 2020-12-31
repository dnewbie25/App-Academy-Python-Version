def select_long_words(words):
  newarr = []
  for word in words:
    if len(word) > 4:
      newarr.append(word)

  return newarr

print(select_long_words(["what", "are", "we", "eating", "for", "dinner"]))
print(select_long_words(["keep", "coding"]))
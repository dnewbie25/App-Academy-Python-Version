def larger_string(str1, str2):
  if len(str1) > len(str2):
    return str1
  elif len(str2) > len(str1):
    return str2
  else:
    return "the same length"
  
print(larger_string('hola', 'hello'))
print(larger_string('how are', 'your parents'))
print(larger_string('hi', 'hi'))
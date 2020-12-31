def select_odds(numbers):
  newarr = []
  for number in numbers:
    if number % 2 != 0:
      newarr.append(number)

  return newarr

print(select_odds([13, 4, 3, 7, 6, 11]))
print(select_odds([2,4,6]))
# Dictionary is the same as a Hash in Ruby

customer = {
  'name': 'John Smith',
  'age': 30,
  'is_verified': True,
}

print(customer['name'])

customer['birthday'] = 'January 30th'

print(customer)
keys = customer.keys()
print(keys) # dict_keys(['name', 'age', 'is_verified', 'birthday'])
values = customer.values()
print(values) # dict_values(['John Smith', 30, True, 'January 30th'])

for key in customer:
  print(key)

for value in customer:
  print(customer[value])

  # or you can also use

for key in customer.keys():
  print(key)

for value in customer.values():
  print(value)

# and you can use them at the sime time the same way as in Ruby

for key, value in customer.items(): # remember to add items()
  print(f'This is the key:{key} - value:{value}')
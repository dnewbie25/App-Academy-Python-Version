def get_double_age(hash):
    hash['age'] *= 2
    return hash

print(get_double_age({"name":"App Academy", "age":5}))
print(get_double_age({"name":"Ruby", "age":23}))
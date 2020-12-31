def retrieve_values(hash1, hash2, key):
    array = []

    for k, v in hash1.items():
        if k not in array and k == key:
            array.append(v)
        for k2, v2 in hash2.items():
            if k2 == key and v2 not in array and k2 == key:
                array.append(v2)
    
    return array

dog1 = {"name":"Fido", "color":"brown"}
dog2 = {"name":"Spot", "color": "white"}

print(retrieve_values(dog1, dog2, 'name'))
print(retrieve_values(dog1, dog2, 'color'))
def upcase_keys(hash):
    new_hash = {}

    for key in hash.keys():
        if key not in new_hash and key == key.upper():
            new_hash[key] = hash[key]
    
    return new_hash

print(upcase_keys({"make": "Tesla", "MODEL": "S", "Year": 2018, "SEATS": 4}))

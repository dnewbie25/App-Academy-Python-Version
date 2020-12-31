def ae_count(str):
    hash = {}

    arr_from_str = list(str)
    for char in arr_from_str:
        if (char == 'a' or char == 'e') and (char not in hash.keys()):
            hash.update({char: 1})
        elif char == 'a' or char == 'e':
            hash[char] += 1

    return hash

print(ae_count("everyone can program!"))
print(ae_count("keyboard"))
print(ae_count('habia una vez una iguana'))

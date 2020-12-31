def frequent_letters(string):
    hash = {}

    for char in string:
        if char not in hash:
            hash.update({char: 1})
        else:
            hash[char] += 1
    
    arr = []

    for k, v in hash.items():
        if v > 2:
            arr.append(k)

    return arr

print(frequent_letters('mississippi'))
print(frequent_letters('bootcamp'))
def element_count(arr):
    hash = {}

    for item in arr:
        if item not in hash.keys():
            hash.update({item: 1})
        else:
            hash[item] += 1

    return hash

print(element_count(["a", "b", "a", "a", "b"]))
print(element_count(["red", "red", "blue", "green"]))
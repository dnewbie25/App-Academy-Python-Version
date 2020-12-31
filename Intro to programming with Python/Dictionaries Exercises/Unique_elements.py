def unique_elements(arr):
    hash = {}

    for item in arr:
        if item not in hash.keys():
            hash.update({item: 1})
        else:
            hash[item] += 1

    return list(hash) # return the keys only

print(unique_elements(['a', 'b', 'a', 'a', 'b', 'c']))
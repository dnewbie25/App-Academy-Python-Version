def element_replace(arr, hash):
    newarr = []

    for item in arr:
        for key, value in hash.items():
            if item == key:
                newarr.append(value)
            elif item not in hash.keys() and item not in newarr:
                newarr.append(item)

    return newarr

arr1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
hash1 = {"Serena Williams":"tennis", "LeBron James":"basketball"}
print(element_replace(arr1, hash1)) # : ["basketball", "Lionel Messi", "tennis"]


arr2 = ["dog", "cat", "mouse"]
hash2 = {"dog":"bork", "cat":"meow", "duck":"quack"}
print(element_replace(arr2, hash2)) # : ["bork", "meow", "mouse"]

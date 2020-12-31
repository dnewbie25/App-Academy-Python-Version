def hash_to_pairs(hash):
    arr = []

    for k, v in hash.items():
        arr.append([k, v])

    return arr

print(hash_to_pairs({"name":"skateboard", "wheels":4, "weight":"7.5 lbs"}))
print(hash_to_pairs({"kingdom":"animalia", "genus":"canis", "breed":"German Shepherd"}))
def get_full_name(hash):
    return hash['first'] + ' ' + hash['last'] + ', the ' + hash['title']

hash1 = {"first":"Michael", "last":"Jordan", "title": "GOAT"}
hash2 = {"first":"Fido", "last":"McDog", "title": "Loyal"}

print(get_full_name(hash1))
print(get_full_name(hash2))
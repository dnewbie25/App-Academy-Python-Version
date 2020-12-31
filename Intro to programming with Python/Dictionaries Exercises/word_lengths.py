def word_lengths(sentence):
    words = {}

    arr = sentence.split(' ')

    for item in arr:
        words[item] = len(item)

    return words

print(word_lengths('this is fun'))
def hand_score(hand):
    hand = hand.upper()

    total = 0

    hash = {
        'A':4,
        'Q': 2,
        'K': 3,
        'J':1,
    }

    for char in hand:
        if char in hash:
            total += hash[char]

    return total

print(hand_score('AQAJ'))
print(hand_score('jJka'))
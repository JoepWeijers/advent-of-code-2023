import functools
from collections import Counter

def strings_to_ints(list):
    return [int(x) for x in list]

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def worth(hand1):
    # 6 5 of a kind
    # 5 4 of a kind
    # 4 full house
    # 3 3 of a kind
    # 2 two pair
    # 1 pair
    # 0 high card

    counter = Counter(hand1)
    hasPair = False
    hasTriple = False
    num_jokers = counter.get('J', 0)
    used_jokers = False
    for key, val in reversed(sorted(counter.items(), key=lambda x: x[1])):
        if key == 'J':
            if val == 5:
                return 6
            continue
        if not used_jokers:
            val += num_jokers
            used_jokers = True
        if val == 5:
            return 6
        if val == 4:
            return 5
        if val == 3:
            hasTriple = True
        if val == 2:
            if hasPair:
                return 2
            hasPair = True
    
    if hasPair and hasTriple:
        return 4
    if hasTriple:
        return 3
    if hasPair:
        return 1
    return 0

def compare(hand1, hand2):
    w1 = worth(hand1)
    w2 = worth(hand2)
    # print(f'{hand1} : {w1}')
    # print(f'{hand2} : {w2}')
    if w1 == w2:
        for index, c in enumerate(hand1):
            if cards.index(c) == cards.index(hand2[index]):
                continue
            return cards.index(hand2[index]) - cards.index(c)

    return w1 - w2

hands = []
bids = {}
f = open('input7.txt', 'r')
for line in f.read().splitlines():
    split = line.split(" ")
    hands.append(split[0])
    bids[split[0]] = int(split[1])

hands.sort(key=functools.cmp_to_key(compare))
print(hands)

#247976779 too low
#247867390 too low

score = 0
for index, hand in enumerate(hands):
    print(f'{hand} : {index + 1} * {bids[hand]}')
    score += (index + 1) * bids[hand]

print(score)
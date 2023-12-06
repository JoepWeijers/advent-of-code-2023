def strings_to_ints(list):
    return [int(x) for x in list]

f = open('input4.txt', 'r')
lines = f.read().splitlines()
num_cards = len(lines)
copies = [1] * num_cards
for line in lines:
    line = line.replace('Card ', '', 1)
    split = line.split(':')
    id = int(split[0]) - 1
    number_sets = split[1].split('|')
    winning_numbers = strings_to_ints(number_sets[0].split())
    my_numbers = strings_to_ints(number_sets[1].split())
    matches = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            matches += 1

    for won_card_id in range(id + 1, id + 1 + matches):
        copies[won_card_id] += copies[id]
    
    print(copies)

        
print(copies)
print(sum(copies))

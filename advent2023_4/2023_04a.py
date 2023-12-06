answer = 0

def strings_to_ints(list):
    return [int(x) for x in list]

f = open('input4.txt', 'r')
for line in f.read().splitlines():
    line = line.replace('Card ', '', 1)
    split = line.split(':')
    id = int(split[0])
    number_sets = split[1].split('|')
    winning_numbers = strings_to_ints(number_sets[0].split())
    my_numbers = strings_to_ints(number_sets[1].split())
    matches = -1
    for my_number in my_numbers:
        if my_number in winning_numbers:
            matches += 1

    if matches != -1:
        answer += 2 ** matches

print(answer)

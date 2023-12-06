import sys

seeds =  [];
maps = [];

def map_to(mappings, number):
    for mapping in mappings:
        if mapping[1] <= number and number < mapping[1] + mapping[2]:
            return number + mapping[0] - mapping[1]
    return number

def strings_to_ints(list):
    return [int(x) for x in list]

map_index = -1
f = open('input.txt', 'r')
for line in f.read().splitlines():
    if line.startswith('seeds'):
        seeds = strings_to_ints(line.split(' ')[1:])
    elif line == '':
        continue
    else:
        if ('map' in line):
            map_index += 1
            maps.append([])
        else:
            maps[map_index].append(strings_to_ints(line.split(' ')))

minimum = sys.maxsize
for seed in seeds:
    number = seed
    for map in maps:
        number = map_to(map, number)
    if number < minimum:
        minimum = number

print(minimum)
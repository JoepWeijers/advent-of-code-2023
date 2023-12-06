import sys, time

seeds =  [];
maps = [];

def split_range(range, split_point):
    rest = split_point - range[0]
    if rest >= range[1]:
        return [range]
    else:
        return [[range[0], rest], [range[0] + rest, range[1] - rest]]

def transform_range(from_range, using_mapping):
    assert from_range[1] <= using_mapping[2]
    return [from_range[0] + using_mapping[0] - using_mapping[1], from_range[1]]

def map_range_to(mappings, original_range):
    # print(f'map range to {original_range} using {mappings}')
    unmapped_ranges = [original_range]
    mapped_ranges = []
    while unmapped_ranges:
        range = unmapped_ranges[0]
        # print(f'checking {range}')
        for mapping in mappings:
            # print(f'trying {range} in {mapping}')
            split_point = mapping[1] + mapping[2]
            if range[0] + range[1] <= mapping[1] or split_point <= range[0]:
                # fully out of range
                # print('out of range')
                pass
            
            elif mapping[1] <= range[0] and range[0] + range[1] <= split_point:
                # fully in range, apply the range transformation
                unmapped_ranges.remove(range)
                mapped_ranges.append(transform_range(range, mapping))
                # print(f'fully in range transforming to {transform_range(range, mapping)}')
                break
                
            # check if we should split
            elif range[0] < mapping[1]:
                unmapped_ranges.remove(range)
                before_and_in = split_range(range, mapping[1])
                # before and in
                unmapped_ranges.append(before_and_in[0])
                if range[0] + range[1] <= split_point:
                    mapped_ranges.append(transform_range(before_and_in[1], mapping))
                    # print(f'{mapping[1]} before {before_and_in[0]} and in {before_and_in[1]} range transforming to {transform_range(before_and_in[1], mapping)}')
                # before in and after
                else:
                    in_and_after = split_range(before_and_in[1], split_point)
                    mapped_ranges.append(transform_range(in_and_after[0], mapping))
                    # print(f'before {before_and_in[0]} in {in_and_after[0]} and after {in_and_after[1]} range transforming to {transform_range(in_and_after[0], mapping)}')
                    unmapped_ranges.append(in_and_after[1])
                break

            # in and after
            elif range[0] + range[1] > split_point:
                unmapped_ranges.remove(range)
                in_and_after = split_range(range, split_point)
                mapped_ranges.append(transform_range(in_and_after[0], mapping))
                # print(f'in {in_and_after[0]} and after {in_and_after[1]} range transforming to {transform_range(in_and_after[0], mapping)}')
                unmapped_ranges.append(in_and_after[1])
                break
        
        if range in unmapped_ranges:
            # print(f'Not mapped {range}')
            unmapped_ranges.remove(range)
            mapped_ranges.append(range)

    # non-matched ranges stay the same
    return mapped_ranges

def map_to(mappings, number):
    for mapping in mappings:
        if mapping[1] <= number and number < mapping[1] + mapping[2]:
            return number + mapping[0] - mapping[1]
    return number

def strings_to_ints(list):
    return [int(x) for x in list]

map_index = -1
f = open('input5.txt', 'r')
for line in f.read().splitlines():
    if line.startswith('seeds'):
        pairs_of_seeds = strings_to_ints(line.split(' ')[1:])
        previous = 0
        for index, item in enumerate(pairs_of_seeds):
            if index % 2 == 0:
                previous = item
            else:
                seeds.append([previous, item])
    elif line == '':
        continue
    else:
        if ('map' in line):
            map_index += 1
            maps.append([])
        else:
            maps[map_index].append(strings_to_ints(line.split(' ')))

print(seeds)
print(split_range([48, 50], 50))
print(split_range([48, 5], 50))
print(split_range([48, 4], 50))
print(split_range([48, 3], 50))
print(split_range([48, 2], 50))
print(split_range([48, 1], 50))
print(split_range([48, 1], 48))

mapped_ranges = []
minimum = sys.maxsize
for seed in seeds:
    print(f'doing seeds {seed}')
    mapped_ranges = [seed]
    for map in maps:
        next_map = []
        print(f'map: {map}, looking for: {mapped_ranges}')
        for range in mapped_ranges:
            next_map.extend(map_range_to(map, range))
        mapped_ranges = next_map.copy()
        print(f'mapped ranges for {map}: {mapped_ranges}')

    for range in mapped_ranges:
        if range[0] < minimum:
            minimum = range[0]

# map range to [68, 13] using [[0, 69, 1], [1, 0, 69]]
# print(map_range_to([[0, 69, 1], [1, 0, 69]], [68, 13]))


print(minimum)

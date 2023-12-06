answer = 0

def add_to_numbers_map(numbers_map, number, x, num_start, num_end):
    # print(f'to_part_number({number}, {x}, {num_start}, {num_end})')
    for y in range(num_start, num_end):
        numbers_map[x][y] = number

def to_gear_ratio(number_map, x, y):
    # print(f'to_part_number({number}, {x}, {num_start}, {num_end})')
    first_number = 0
    for check_x in range(x - 1, x + 2):
        if check_x == -1 or check_x == len(map):
            continue

        for check_y in range(y - 1, y + 2):
            if check_y == -1 or check_y == len(map[0]):
                continue

            number = number_map[check_x][check_y]
            if number:
                print(f'Gear at {x}, {y}: {number}')
                if first_number == 0:
                    first_number = number
                elif number != first_number:
                    print(f'Gear ratio at {x}, {y}: {first_number * number}')
                    return first_number * number
    
    print(f'Not gear at {x}, {y}')
    return 0

f = open('input3.txt', 'r')
map = []
numbers_map = []
lines = f.read().splitlines()
for line in lines:
    map.append(list(line))
    numbers_map.append([None] * len(line))

for x, line in enumerate(lines):
    number = ''
    num_start = -1
    num_end = 0
    for y, c in enumerate(line):
        if c.isdigit():
            number += c
            if num_start == -1:
                num_start = y
        
        if not c.isdigit() or y == len(line) - 1:
            if num_start != -1:
                num_end = y
                add_to_numbers_map(numbers_map, int(number), x, num_start, num_end)
                num_start = -1
                number = ''

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '*':
            answer += to_gear_ratio(numbers_map, x, y)

print(answer)
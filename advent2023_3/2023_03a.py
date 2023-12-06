answer = 0

def to_part_number(map, number, x, num_start, num_end):
    # print(f'to_part_number({number}, {x}, {num_start}, {num_end})')
    for check_x in range(x - 1, x + 2):
        if check_x == -1 or check_x == len(map):
            continue

        for check_y in range(num_start - 1, num_end + 2):
            if check_y == -1 or check_y == len(map[0]):
                continue

            # print(f'checking {check_x},{check_y}: {map[check_x][check_y]}')
            if not map[check_x][check_y].isdigit() and map[check_x][check_y] != '.':
                print(f'Yes {number}')
                return number
    
    print(f'Not {number}')
    return 0

f = open('input3.txt', 'r')
map = []
lines = f.read().splitlines()
for line in lines:
    map.append(list(line))

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
                num_end = y - 1
                answer += to_part_number(map, int(number), x, num_start, num_end)
                num_start = -1
                number = ''

print(answer)

# 8358597 too high
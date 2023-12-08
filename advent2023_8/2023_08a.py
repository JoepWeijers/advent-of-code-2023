import re

def strings_to_ints(list):
    return [int(x) for x in list]

pattern = re.compile(r'^\(([A-Z]+), ([A-Z]+)\)$')

f = open('input8.txt', 'r')
lines = f.read().splitlines()
directions = lines[0]
nodes = {}
for line in lines[2:]:
    split = line.split(" = ")
    matcher = pattern.search(split[1])
    nodes[split[0]] = (matcher.group(1), matcher.group(2))

steps = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    dir = directions[steps % len(directions)]
    steps += 1
    if (dir == 'L'):
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]

print(steps)
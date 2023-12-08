import re

def strings_to_ints(list):
    return [int(x) for x in list]

pattern = re.compile(r'^\(([0-9A-Z]+), ([0-9A-Z]+)\)$')

f = open('input8.txt', 'r')
lines = f.read().splitlines()
directions = lines[0]
nodes = {}
current_nodes = []
for line in lines[2:]:
    split = line.split(" = ")
    matcher = pattern.search(split[1])
    if split[0][-1] == 'A':
        current_nodes.append(split[0])
    
    nodes[split[0]] = (matcher.group(1), matcher.group(2))

def all_nodes_end_in_z(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

print(current_nodes)
steps = 0
while not all_nodes_end_in_z(current_nodes):
    dir = directions[steps % len(directions)]
    steps += 1
    new_nodes = []
    for current_node in current_nodes:
        if (dir == 'L'):
            new_nodes.append(nodes[current_node][0])
        else:
            new_nodes.append(nodes[current_node][1])

#    print(f'{steps}: {new_nodes}')
    current_nodes = new_nodes

print(steps)
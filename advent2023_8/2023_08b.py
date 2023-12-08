import re
import math

def lcm_of_list(numbers):
    def prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    all_factors = {}
    for num in numbers:
        factors = prime_factors(num)
        unique_factors = set(factors)
        for factor in unique_factors:
            count = factors.count(factor)
            if factor not in all_factors or count > all_factors[factor]:
                all_factors[factor] = count

    lcm = 1
    for factor, count in all_factors.items():
        lcm *= int(math.pow(factor, count))

    return lcm

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

print(current_nodes)
steps_to_end = []
for current_node in current_nodes:
    steps = 0
    while current_node[-1] != 'Z':
        dir = directions[steps % len(directions)]
        steps += 1
        if (dir == 'L'):
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
    steps_to_end.append(steps)

print(steps_to_end)
print(lcm_of_list(steps_to_end))
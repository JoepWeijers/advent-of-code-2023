import re

def strings_to_ints(list):
    return [int(x) for x in list]

f = open('input1.txt', 'r')
answer = 0
pattern = re.compile(r'^[a-z]*(\d)?[a-z0-9]*(\d)[a-z]*$')
for line in f.read().splitlines():
    print(line)
    result = pattern.search(line)
    first = result.group(2)
    if result.group(1):
        first = result.group(1)
    print(first + result.group(2))
    answer += int(first + result.group(2))

print(answer)

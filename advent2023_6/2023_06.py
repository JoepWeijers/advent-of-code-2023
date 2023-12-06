import re

def strings_to_ints(list):
    return [int(x) for x in list]

time = []
records = []
f = open('input6b.txt', 'r')
for line in f.read().splitlines():
    if line.startswith('Time:'):
        time = strings_to_ints(re.split('\s+', line)[1:])
    elif line.startswith('Distance:'):
        records = strings_to_ints(re.split('\s+', line)[1:])

answer = 1
for i, item in enumerate(time):
    print(item, records[i])
    farther = 0
    for ms in range(item):
        distance = ms * (item - ms)
        if distance > records[i]:
            farther += 1
    print(farther)
    answer *= farther

print(answer)

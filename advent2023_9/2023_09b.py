def strings_to_ints(list):
    return [int(x) for x in list]

f = open('input9.txt', 'r')
lines = f.read().splitlines()

answer = 0
for line in lines:
    history = strings_to_ints(line.split())
    history.reverse()

    diffs = []
    list = history
    to_add = history[-1]
    while not all(y == 0 for y in list):
        diff = []
        for i in range(1, len(list)):
            delta = list[i] - list[i - 1]
            diff.append(delta)

        diffs.append(diff)
        list = diff
        to_add += diff[-1]
    answer += to_add

print(answer)

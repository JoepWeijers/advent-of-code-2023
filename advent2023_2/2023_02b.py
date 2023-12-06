answer = 0

f = open('input2.txt', 'r')
for line in f.read().splitlines():
    max_green = 0
    max_red = 0
    max_blue = 0

    line = line.replace('Game ', '', 1)
    split = line.split(':')
    id = int(split[0])
    outcomes = split[1].split(';')
    for outcome in outcomes:
        colors = outcome.split(',')
        for color in colors:
            num_and_color = color.strip().split(' ')
            num = int(num_and_color[0])
            if num_and_color[1] == 'green' and num > max_green:
                max_green = num
            elif num_and_color[1] == 'red' and num > max_red:
                max_red = num
            elif num_and_color[1] == 'blue' and num > max_blue:
                max_blue = num

    print(max_green * max_red * max_blue)
    answer += max_green * max_red * max_blue
    

print(answer)

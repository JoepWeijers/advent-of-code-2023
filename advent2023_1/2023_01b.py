def text_to_number(rest_of_line):
    if (rest_of_line.startswith('one')):
        return '1'
    elif (rest_of_line.startswith('two')):
        return '2'
    elif (rest_of_line.startswith('three')):
        return '3'
    elif (rest_of_line.startswith('four')):
        return '4'
    elif (rest_of_line.startswith('five')):
        return '5'
    elif (rest_of_line.startswith('six')):
        return '6'
    elif (rest_of_line.startswith('seven')):
        return '7'
    elif (rest_of_line.startswith('eight')):
        return '8'
    elif (rest_of_line.startswith('nine')):
        return '9'

def text_to_number_reversed(rest_of_line):
    if (rest_of_line.startswith('eno')):
        return '1'
    elif (rest_of_line.startswith('owt')):
        return '2'
    elif (rest_of_line.startswith('eerht')):
        return '3'
    elif (rest_of_line.startswith('ruof')):
        return '4'
    elif (rest_of_line.startswith('evif')):
        return '5'
    elif (rest_of_line.startswith('xis')):
        return '6'
    elif (rest_of_line.startswith('neves')):
        return '7'
    elif (rest_of_line.startswith('thgie')):
        return '8'
    elif (rest_of_line.startswith('enin')):
        return '9'

f = open('input1.txt', 'r')
answer = 0
for line in f.read().splitlines():
    for index, c in enumerate(line):
        if c.isdigit():
            first = c
            break
        number = text_to_number(line[index:])
        if number:
            first = number
            break
    
    reversed = list(line)
    reversed.reverse()
    for index, c in enumerate(reversed):
        if c.isdigit():
            last = c
            break
        number = text_to_number_reversed(''.join(reversed)[index:])
        if number:
            last = number
            break
    
    print(first + last)
    answer += int(first + last)

print(answer)


def solve():
    pos = [0,0]
    aim = 0
    ins = [x.split(' ') for x in open('day2.txt') if x != '']
    for line in ins:
        if line[0] == 'forward':
            pos[0] += int(line[1])
            pos[1] += (aim * int(line[1]))
        elif line[0] == 'up':
            aim -= int(line[1])
        else:
            aim += int(line[1])

    return pos[0] * pos[1]

print(solve())
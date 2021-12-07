from GetInput import GetInput

def solve():
    d = GetInput()
    d.get_input(1)
    count = 0
    spot = 0
    rows = [int(x) for x in open('day1.txt')]
    while spot < len(rows[:-1]):
        if rows[spot] == '':
            spot += 1
            continue
        else:
            if rows[spot + 1] > rows[spot]: 
                count += 1
                spot += 1
            else:
                spot += 1
    print(count)

solve()
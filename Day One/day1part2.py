
def solve():
    rows = [int(x) for x in open('day1.txt') if x != '']
    sums = []
    spot = 0
    while spot + 3 <= len(rows):
        sums.append(sum(rows[spot:spot+3]))
        spot += 1

    count = 0
    sums_spot = 0
    while sums_spot < len(sums[:-1]):
        if sums[sums_spot] == '':
            sums_spot += 1
            continue
        else:
            if sums[sums_spot + 1] > sums[sums_spot]: 
                count += 1
                sums_spot += 1
            else:
                sums_spot += 1
    print(count)

solve()
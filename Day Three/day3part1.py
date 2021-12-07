from GetInput import GetInput
from collections import Counter, defaultdict

def solve():
    d = GetInput()
    d.get_input(3)
    nums = [x for x in open('day3.txt')]
    bits = defaultdict(list)
    for num in nums:
        spot = 0
        while spot < len(num):
            if num[spot] == '\n': 
                spot += 1
                continue
            bits[spot].append(num[spot])
            spot += 1

    gamma = ''
    epsilon = ''

    for y in bits.values():
        counts = Counter(y).most_common()
        gamma += counts[0][0]
        epsilon += counts[-1][0]

    print(gamma)
    print(f'Power Consumption: {int(gamma, 2) * int(epsilon, 2)}')


solve()
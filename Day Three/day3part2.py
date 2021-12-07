# from collections import Counter, defaultdict

# NUMS = [x.rstrip() for x in open('day3.txt')]

# def get_most_least_common(nums):
#     bits = defaultdict(list)
#     for num in nums:
#         spot = 0
#         while spot < len(num):
#             if num[spot] == '\n': 
#                 spot += 1
#                 continue
#             bits[spot].append(num[spot])
#             spot += 1

#     gamma = ''
#     epsilon = ''

#     for y in bits.values():
#         counts = Counter(y).most_common()
#         gamma += counts[0 if counts[0][1] >= counts[-1][1] else -1][0]
#         epsilon += counts[-1 if counts[-1][1] >= counts[0][1] else 0][0]

#     # print(gamma)
#     # print(epsilon)

#     return [gamma, epsilon, counts]

# def solve():
    
#     def find_o2():
#         filtered_nums = []
#         spot = 0
#         while spot < 12:
#             if len(filtered_nums) == 1: break
#             if spot == 0:
#                 most, least, counts = get_most_least_common(NUMS)
#                 filtered_nums = [x for x in NUMS if x.startswith(most[spot])]
#                 print(f"O2 - {spot} - {counts}")
#             else:
#                 most, least, counts = get_most_least_common(filtered_nums)
#                 print(filtered_nums)
#                 filtered_nums = [x for x in filtered_nums if x[spot] == most[spot]]
#                 print(filtered_nums)
#                 print(f"Most - {most}")
#                 print(f"Least - {least}")
#                 print(f"O2 - {spot} - {counts}")
#             spot += 1

#         # print(filtered_nums)
#         # print(filtered_nums[0][:spot-1])
#         return filtered_nums[0]
    
#     def find_co2():
#         filtered_nums = []
#         spot = 0
#         while spot < 12:
#             if len(filtered_nums) == 1: break
#             if spot == 0:
#                 most, least, counts = get_most_least_common(NUMS)
#                 filtered_nums = [x for x in NUMS if x.startswith(least[spot])]
#                 # print(f"CO2 - {spot} - {counts}")
#             else:
#                 most, least, counts = get_most_least_common(filtered_nums)
#                 filtered_nums = [x for x in filtered_nums if x[spot] == least[spot]]
#                 # print(f"CO2 - {spot} - {counts}")
#             spot += 1
    
#         # print(filtered_nums)
#         # print(filtered_nums[0][:spot-1])
#         return filtered_nums[0]

#     # print(find_o2())
#     # print(find_co2())
#     print(int(find_o2(),2) * int(find_co2(),2))


# solve()

from dataclasses import dataclass


@dataclass
class Counter:
    zeros: int = 0
    ones: int = 0

    def common(self):
        return 0 if self.zeros > self.ones else 1

    def least_common(self):
        return 1 if self.zeros > self.ones else 0


def to_decimal(string):
    res = 0
    for i, bit in enumerate(string[::-1]):
        if int(bit) == 1:
            res = res + pow(2,i)
    return res

def part1(input):
    counts = [Counter() for i in range(len(input[0]))]
    for report in input:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
            else:
                raise ValueError()
    gamma = "".join([str(count.common()) for count in counts])
    epsilon = "".join([str(count.least_common()) for count in counts])
    gamma_rate = to_decimal(gamma)
    epsilon_rate = to_decimal(epsilon)
    return gamma_rate * epsilon_rate


def find_rating(reports, rating_type,index):
    if len(reports) == 1:
        return to_decimal(reports[0])
    counts = [Counter() for i in range(len(reports[0]))]
    for report in reports:
        for i, bit in enumerate(report):
            if bit == "0":
                counts[i].zeros += 1
            elif bit == "1":
                counts[i].ones += 1
            else:
                raise ValueError()
    gamma = "".join([str(count.common()) for count in counts])
    if "oxygen" == rating_type:
        return find_rating([report for report in reports if report[index] == gamma[index]], rating_type, index + 1)
    return find_rating([report for report in reports if report[index] != gamma[index]], rating_type, index + 1)


def part2(input):
    oxygen = find_rating(input, "oxygen", 0)
    co2 = find_rating(input, "co2", 0)
    print(oxygen * co2)


def main():
    with open("day3.txt", "r") as f:
        lines = f.read().splitlines()
        print(part1(lines))
        print(part2(lines))

if __name__ == '__main__':
    main()
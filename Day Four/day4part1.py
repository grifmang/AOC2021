from collections import defaultdict

picks = None
grids = {}


def build_matrices():
    global picks, grids
    with open('day4.txt') as file:
        index = count = 0
        temp_rows = []
        for line in file:
            line = ' '.join(line.rstrip().split())
            if index == 0:
                picks = [int(x) for x in line.split(',')]
            else:
                if line != '':
                    temp_rows.append([int(x) for x in line.split(' ')])
                else:
                    if index != 1:
                        grids[count] = {
                            'nums': temp_rows,
                            'matches': [[0 for _ in range(5)] for _ in range(5)]
                        }
                        count += 1
                        temp_rows = []

            index += 1
        
        if len(temp_rows):
            grids[count] = {
                'nums': temp_rows,
                'matches': [[0 for _ in range(5)] for _ in range(5)]
            }

def get_column(matrix, col):
    return [row[col] for row in matrix]

def check_winner(pick):
    global grids
    for match in grids.values():
        for row in match['matches']:
            if sum(row) == 5:
                return [True, determine_answer(match['nums'], match['matches'], pick)]

        for num in range(5):
            if sum(get_column(match['matches'], num)) == 5:
                return [True, determine_answer(match['nums'], match['matches'], pick)]

    return [False, 0]

def determine_answer(matrix, matches, pick):
    answer = 0
    for row in range(5):
        for col in range(5):
            if matches[row][col] != 1:
                answer += matrix[row][col]

    return answer * pick

def mark_matches(pick):
    global grids
    matched = False
    for grid in grids.values():
        row = index = 0
        while row < 5:
            if pick in grid['nums'][row]:
                index = grid['nums'][row].index(pick)
                grid['matches'][row][index] = 1
                matched = True
            row += 1
    return matched


def solve():
    build_matrices()
    global grids, picks
    for pick in picks:
        match = mark_matches(pick)
        if match:
            winner, answer = check_winner(pick)
            if winner: return answer

print(solve())
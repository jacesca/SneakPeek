#!/usr/bin/python
"""
Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time in any
of the four directions. Can you rescue the princess?

Input format
- The first line contains an odd integer N (3 <= N < 100) denoting the size
  of the grid. This is followed by an NxN grid. Each cell is denoted by '-'
  (ascii value: 45). The bot position is denoted by 'm' and the princess
  position is denoted by 'p'.
- Grid is indexed using Matrix Convention

Output format
- Print out the moves you will take to rescue the princess in one go.
  The moves must be separated by '\n', a newline. The valid moves are LEFT
  or RIGHT or UP or DOWN.

Sample input
3

---
-m-
p--

Sample output
DOWN
LEFT

Task
- Complete the function displayPathtoPrincess which takes in two parameters -
  the integer N and the character array grid. The grid will be formatted
  exactly as you see it in the input, so for the sample input the princess is
  at grid[2][0].
  The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive
  lines to rescue/reach the princess. The goal is to reach the princess in as
  few moves as possible.
- The above sample input is just to help you understand the format. The
  princess ('p') can be in any one of the four corners.

Scoring
- Your score is calculated as follows : (NxN - number of moves made to rescue
  the princess)/10, where N is the size of the grid (3x3 in the sample
  testcase).
https://www.hackerrank.com/challenges/saveprincess/submissions/game/380249419
"""
# import numpy as np


def displayPathtoPrincess(n, grid):
    # print all the moves here
    # mi, mj = np.array(np.where(grid == 'm')).ravel()
    # pi, pj = np.array(np.where(grid == 'p')).ravel()
    # mi, mj = list(sum([(row, col.split().index('m')) for row, col in enumerate(grid) if 'm' in col], ()))  # noqa
    # pi, pj = list(sum([(row, col.replace(' ', '').index('p')) for row, col in enumerate(grid) if 'p' in col], ()))  # noqa
    mi, mj = n // 2, n // 2
    pi, pj = list(sum([(row, col.index('p')) for row, col in enumerate(grid) if 'p' in col], ()))  # noqa

    while True:
        # print((mi, mj), (pi, pj))
        if pi == mi:
            if pj == mj:
                break
            elif pj > mj:
                print('RIGHT')
                mj += 1
            elif pj < mj:
                print('LEFT')
                mj -= 1
        elif pi > mi:
            print('DOWN')
            mi += 1
        else:
            print('UP')
            mi -= 1


# input: 3
#        ---
#        -m-
#        --p
# output: DOWN
#         RIGHT

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())
print(grid)
# m = 3
# grid = ['---', '-m-', '--p']

displayPathtoPrincess(m, grid)

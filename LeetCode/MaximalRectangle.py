"""Maximal Rectangle
Given a rows x cols binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.
"""
from collections import namedtuple
from collections import Counter
from itertools import chain
from pprint import pprint
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == [['1']]:
            return 1
        if len(Counter(chain(*matrix))) == 1 and matrix[0][0] == '1':
            return len(matrix) * len(matrix[0])
        if matrix == [['0']] or (
            len(Counter(chain(*matrix))) == 1
            and matrix[0][0] == '0'
        ):
            return 0

        Point = namedtuple('Point', ['row', 'col'])
        rect = {}
        direction = ['corner', 'left', 'top']

        def get_area(i, j, i0, j0):
            return (j-j0+1) * (i-i0+1)

        def find_ij(i, j, d, origin):
            """Find the minimal i and j with value 1 in a row o column.
            i: int. row of the matrix.
            j: int. column of the matrix
            d: string. It shows the direction. It can be: left, top, or corner.
            d describe the direction
            origin: point(row, col), return the starting point.
            Output: size of the biggest found rectanle
            """
            if d in 'corner':
                loc_corner = {}
                if i > 0 and j > 0 and all([
                        matrix[x][y] == '1'
                        for x in range(i-1, origin.row+1)
                        for y in range(j-1, origin.col+1)
                ]):
                    itemp, jtemp = find_ij(i-1, j-1, 'corner', origin)
                    loc_corner[itemp, jtemp] = get_area(origin.row, origin.col, itemp, jtemp)  # noqa
                if j > 0 and all([matrix[x][j-1] == '1' for x in range(i, origin.row+1)]):  # noqa
                    itemp, jtemp = find_ij(i, j-1, 'corner', origin)
                    loc_corner[itemp, jtemp] = get_area(origin.row, origin.col, itemp, jtemp)  # noqa
                if i > 0 and all([matrix[i-1][y] == '1' for y in range(j, origin.col+1)]):  # noqa
                    itemp, jtemp = find_ij(i-1, j, 'corner', origin)
                    loc_corner[itemp, jtemp] = get_area(origin.row, origin.col, itemp, jtemp)  # noqa
                if loc_corner:
                    return max(loc_corner, key=loc_corner.get)

            elif d == 'left':
                if i > 0 and matrix[i-1][j] == '1':
                    return find_ij(i-1, j, 'left', origin)
            elif d == 'top':
                if j > 0 and matrix[i][j-1] == '1':
                    return find_ij(i, j-1, 'top', origin)
            return i, j

        def get_larger(rect):
            return max([item[1][1] for item in rect.items()])

        i, j = 0, 0
        while i < len(matrix):
            while j < len(matrix[0]):
                p = Point(i, j)
                if rect == {}:
                    if matrix[i][j] == '1':
                        for d in direction:
                            rect[(p, d)] = (p, 1)
                elif matrix[i][j] == '1':
                    for d in direction:
                        i0, j0 = find_ij(i, j, d, p)
                        a = get_area(i, j, i0, j0)
                        if (Point(i0, j0), d) in rect.keys():
                            if a < rect[(Point(i0, j0), d)][1]:
                                continue
                        rect[(Point(i0, j0), d)] = (p, a)
                j += 1
            i += 1
            j = 0
        # pprint(rect)
        return get_larger(rect)


test_cases = [
    # [["1", "0", "1", "0", "0"],
    #  ["1", "0", "1", "1", "1"],
    #  ["1", "1", "1", "1", "1"],
    #  ["1", "0", "0", "1", "0"]],
    # [["0"]],
    # [["1"]],
    # [["0", "0"]],
    # [["1", "0", "0", "0", "1"],
    #  ["1", "1", "0", "1", "1"],
    #  ["1", "1", "1", "1", "1"]],
    # [["1", "1", "0", "1"],
    #  ["1", "1", "0", "1"],
    #  ["1", "1", "1", "1"]],
    # [["1", "1", "1", "1", "1", "1", "1", "1"],
    #  ["1", "1", "1", "1", "1", "1", "1", "0"],
    #  ["1", "1", "1", "1", "1", "1", "1", "0"],
    #  ["1", "1", "1", "1", "1", "0", "0", "0"],
    #  ["0", "1", "1", "1", "1", "0", "0", "0"]],
    [["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],  # noqa
     ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],  # noqa
     ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],  # noqa
     ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0"],  # noqa
     ["1", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1"],  # noqa
     ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1"],  # noqa
     ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],  # noqa
     ["1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1"]]  # noqa
]

for test_case in test_cases:
    pprint(Solution().maximalRectangle(test_case))

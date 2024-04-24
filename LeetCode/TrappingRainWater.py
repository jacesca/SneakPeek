"""Trapping Rain Water
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it
can trap after raining.
3                           |||||
2                           |||||
1            ||||===|===|===|||||||||===|||||
0    |||||===||||||||   ||||||||||||||||||||||||||
--------------------------------------------------------
[ 0   1    0   2   1  0   1   3   2    1  2    1 ]
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is
represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this
case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        w = len(height)
        c = 0
        for i in range(1, w-1):
            al = max(height[:i])
            ar = max(height[i+1:])
            if not (i in [0, w-1]) and al > height[i] < ar:
                c += (min(al, ar) - height[i])
        return c


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([2, 0, 2]))
print(Solution().trap([2, 1, 2, 6, 9, 7, 5, 5, 7]))
print(Solution().trap([0, 2, 8, 2, 9, 7, 4]))

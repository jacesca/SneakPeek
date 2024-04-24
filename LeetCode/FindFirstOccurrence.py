"""Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1


test_cases = [
    ("sadbutsad", "sad"),
    ("leetcode", "leeto")
]
for haystack, needle in test_cases:
    print(Solution().strStr(haystack, needle))

"""
Time complexity:
    The time complexity depends on the operation of searching for the needle
    string within the haystack string.
    - Checking if the needle is in the haystack:
        In Python's built-in in operator or index() method, this search
        operationis optimized and generally runs in O(n + m) time complexity,
        where n is the length of the haystack string and m is the length of
        the needle string.
    - Finding the index of the needle in the haystack:
        If the needle is found in the haystack, returning its index involves
        additional constant-time operations.
    Therefore, the overall time complexity of the strStr method is O(n + m),
    where n is the length of the haystack string and m is the length of the
    needle string.

Space complexity:
    The space complexity of this code is O(1) because it does not use any
    additional space that grows with the size of the input strings. Regardless
    of the size of the input strings haystack and needle, the space usage
    remains constant.

    The method simply checks if the needle string is a substring of the
    haystack string, and if so, it returns the index of the first occurrence.
    There are no additional data structures or variables created that depend
    on the size of the input strings. Therefore, the space complexity is
    constant, or O(1).

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/5015314/no-more-variables-required-to-solve-it/
    Runtime: 33 ms (Beats 71.56% of users with Python3)
    Memory: 16.52 MB (Beats 43.32% of users with Python3)
"""

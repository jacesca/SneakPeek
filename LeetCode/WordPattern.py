"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
from collections import Counter
from functools import reduce


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pc = list(map(str.upper, dict(Counter(str(pattern))).keys()))
        sa = list(dict(Counter(str(s).split(' '))).keys())
        result = str(s).split(' ')
        if len(sa) != len(pc):
            return False
        for i in range(len(pc)):
            result = [pc[i] if val == sa[i] else val for val in result]

        return str(pattern) == ''.join(result).lower()


print(Solution().wordPattern("abc", "b c a"))
# print(Solution().wordPattern(input(), input()))
print(Solution().wordPattern("deadbeef", "d e a d b e e f"))
print(Solution().wordPattern("abba", "dog dog dog dog"))


repls = {'hello': 'goodbye', 'goodbye': 'earth'}
s = 'hello, goodbye'
print(reduce(lambda a, kv: a.replace(*kv), repls.items(), s))

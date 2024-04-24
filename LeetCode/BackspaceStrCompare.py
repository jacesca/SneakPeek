"""Backspace String Compare
Given two strings s and t, return true if they are
equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text
will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""
import re


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pattern = r"[^#]#|^#"
        while re.search(pattern, s) or re.search(pattern, t):
            # print(re.findall(pattern, s), re.findall(pattern, t))
            s = re.sub(pattern, '', s)
            t = re.sub(pattern, '', t)
        return s == t


print(Solution().backspaceCompare("ab#c", "ad#c"))
print(Solution().backspaceCompare("ab##", "c#d#"))
print(Solution().backspaceCompare("a#c", "b"))
print(Solution().backspaceCompare("a##c", "#a#c"))
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))
print(Solution().backspaceCompare("du###vu##v#fbtu", "du###vu##v##fbtu"))

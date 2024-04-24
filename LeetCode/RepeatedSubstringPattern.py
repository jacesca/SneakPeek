"""
Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring
"abcabc" twice.

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(size//2, 0, -1):
            if size % i == 0:
                print(i, s[:i]*(size // i))
                if s[:i]*(size // i) == s:
                    return True
        return False


print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("aba"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))

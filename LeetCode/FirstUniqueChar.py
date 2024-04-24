"""First Unique Character in a String
Given a string s, find the first non-repeating character
in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict(Counter(s))
        unique_letters = [k for k, v in d.items() if v == 1]
        return s.index(unique_letters[0]) \
            if len(list(unique_letters)) > 0 else -1
        # d = Counter(s)
        # unique_letters = next(filter(lambda item: item[1]==1, d.items()),
        #                       None)
        # return s.index(unique_letters[0]) if unique_letters else -1


test_cases = [
    "leetcode",
    "loveleetcode",
    "aabb",
]
for test_case in test_cases:
    print(Solution().firstUniqChar(test_case))

"""
Complexity
Time complexity:
    The time complexity can be analyzed as follows:
    - Creating the dictionary d using Counter(s):
        This step involves iterating over the string s to count the
        occurrences of each character. The time complexity of this
        step is O(n), where n is the length of the input string s.
    - Creating the list unique_letters:
        This step involves iterating over the dictionary d to extract
        keys (characters) with a count of 1. Since iterating over a
        dictionary takes O(n) time where n is the number of key-value
        pairs in the dictionary, and in the worst case scenario, all
        characters are unique, this step also takes O(n) time.
    - Returning the index of the first unique character:
        This operation involves finding the index of the first
        occurrence of the first unique character in the input string s.
        It requires searching through the string, which can take up to
        O(n) time in the worst case.
    Therefore, the overall time complexity is O(n) + O(n) + O(n) = O(n),
    where n is the length of the input string s.

Space complexity:
    The space complexity can be analyzed as follows:
    - Creating the dictionary d using Counter(s):
        The space complexity of this step depends on the number of
        unique characters in the input string s. In the worst case
        scenario, where all characters are unique, the space
        complexity is O(n), where n is the length of the input string s.
    - Creating the list unique_letters:
        The space complexity of this step depends on the number of unique
        characters in the input string s with a count of 1. In the worst
        case scenario, where all characters are unique, the space
        complexity is also O(n), where n is the length of the input string s.
    - Other variables:
        The space complexity of other variables such as loop indices and
        the return value is O(1), as they occupy a constant amount of space.
    Therefore, the overall space complexity of the firstUniqChar method is
    O(n), where n is the length of the input string s, dominated by the
    space required to store the dictionary d and the list unique_letters.

https://leetcode.com/problems/first-unique-character-in-a-string/solutions/5015190/counter-is-the-key/  # noqa
Runtime: 63 ms (Beats 96.70% of users with Python3)
Memory: 17.28 MB (Beats 38.64% of users with Python3)
"""

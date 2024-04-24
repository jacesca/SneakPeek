"""String to Integer
"""
import re


class Solution:
    import re

    def myAtoi(self, s: str) -> int:
        lim = 2**31
        pattern = r'[-+]?[0-9]+'

        s = s.strip()
        if (
            s != '' and s[0].isnumeric() or
            (
                len(s) > 1 and s[0] in ['-', '+']
                and s[1].isnumeric()
            )
        ):
            s = re.findall(pattern, s)
            n = int(s[0]) if s else 0
            if n < -lim:
                return -lim
            elif n > lim - 1:
                return lim - 1
            else:
                return n
        else:
            return 0


test_cases = [
    "42",
    "   -42",
    "4193 with words",
    "words and 987",
    "-91283472332",
    "3.14159",
    "+-12",
    "  +  413"
]
for test_case in test_cases:
    print(Solution().myAtoi(test_case))

"""
Time complexity:
    The time complexity of this code is primarily determined by the
    regular expression matching and the subsequent conversion to an
    integer. Let's break down the main operations:
    - Stripping leading and trailing whitespaces from the input string:
        This operation has a time complexity of O(n), where n is the
        length of the input string.
    - Regular expression matching:
        The regular expression pattern r'[-+]?[0-9]+' is used to find
        the numeric part of the string. The time complexity of
        re.findall() is typically O(n), where n is the length of the
        input string.
    - Integer conversion:
        Converting the extracted substring to an integer has a time
        complexity that depends on the length of the substring. In most
        implementations, this operation is O(k), where k is the length
        of the substring.
    Therefore, the overall time complexity of this code is
    O(n) + O(n) + O(k) = O(n + k), where n is the length of the input
    string and k is the length of the numeric substring extracted by
    the regular expression.

Space complexity:
    The space complexity of this code primarily depends on the space
    required to store intermediate variables and the output integer.
    Let's break it down:
    - Regular expression matches:
        The re.findall() function might create a list containing the
        matched substrings. The space required for this list depends
        on the number of matches found in the input string. In the
        worst case, if the entire input string consists of numeric
        characters, this list could potentially contain one substring,
        resulting in O(1) space. However, in the worst-case scenario
        where there are multiple numeric substrings separated by
        non-numeric characters, the space complexity could be O(m),
        where m is the number of numeric substrings.
    - Integer conversion:
        The space required to store the integer output (n) is O(1)
        because it's a single integer variable.
    - Other variables:
        The space required to store other variables such as lim,
        pattern, and loop indices is O(1) since these are fixed-size
        variables.
    Overall, considering the worst-case scenario where there are
    multiple numeric substrings separated by non-numeric characters,
    the space complexity of this code is O(m), where m is the number
    of numeric substrings found in the input string. However, in
    typical cases where there's only one numeric substring, the
    space complexity reduces to O(1).

https://leetcode.com/problems/string-to-integer-atoi/solutions/5014721/using-regular-expressions-to-solve-it/  # noqa
    Runtime: 24ms (Beats 99.16% of users with Python3)
    Memory: 16.48 MB (Beats 97.78% of users with Python3)
"""

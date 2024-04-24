"""
Remove K Digits
Given string num representing a non-negative integer num, and an
integer k, return the smallest possible integer after removing k
digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"

Example 2:
Input: num = "10200", k = 1
Output: "200"
"""
import sys


sys.set_int_max_str_digits(0)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        # Initializing the stack
        stk = []

        for n in num:
            print(k, stk, n)
            # While there are pending removals k
            while k > 0 and stk and n < stk[-1]:
                stk.pop()
                k -= 1
                print('    ', k, stk, n)
            # Adding the current n
            stk.append(n)

        # Confirming remaining removals
        while k > 0 and stk:
            stk.pop()
            k -= 1

        return str(int(''.join(list(map(str, stk)))))


# print(Solution().removeKdigits("1432219", 3))
# print(Solution().removeKdigits("10200", 1))
# print(Solution().removeKdigits("10", 2))
# print(Solution().removeKdigits("112", 1))
# print(Solution().removeKdigits("1234567890", 9))
print(Solution().removeKdigits("9964143", 5))

"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of
its employees. For this we need to create a function for validating all the
randomly generated UIDs.

A valid UID must follow the rules below:
- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0-9).
- It should only contain alphanumeric characters (a-z, A-Z, 0-9).
- No character should repeat.
- There must be exactly 10 characters in a valid UID.

Input Format
    The first line contains an integer , the number of test cases.
    The next  lines contains an employee's UID.

Output Format
    For each test case, print 'Valid' if the UID is valid. Otherwise,
    print 'Invalid', on separate lines.

Sample Input
    2
    B1CD102354
    B1CDEF2354
Sample Output
    Invalid
    Valid

https://www.hackerrank.com/challenges/validating-uid/submissions/code/380410003
"""
import re
# import os


def isValidUID(uidn):
    # Execute the following validation:
    # ^   Start
    # (?=(?=[a-z\d]*[A-Z]){2})        It must contain at least 2 uppercase characters.     # noqa
    # (?=(?:.*\d){3})                 It must contain at least 3 digits.                   # noqa
    # (?:([a-zA-Z\d])(?!.*\1)){10}    It must contain 10 non repeated alphanumeric chars.  # noqa
    # $   End
    pattern = r"^(?=(?=[a-z\d]*[A-Z]){2})(?=(?:.*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"     # noqa
    if len(re.findall(pattern, uidn)) > 0:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == '__main__':
    # Input: 2
    #        B1CD102354
    #        B1CDEF2354
    # Output: Invalid
    #         Valid
    n = int(input().rstrip())
    for _ in range(n):
        uidn = input().strip()
        result = isValidUID(uidn)
        print(result)

    # # Next code is to print in stdout
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().rstrip())
    # for _ in range(n):
    #     uidn = input().strip()
    #     result = isValidUID(uidn)
    #     fptr.write(result)
    #     fptr.write('\n')
    # fptr.close()

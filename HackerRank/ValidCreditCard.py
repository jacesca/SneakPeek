"""
Read from stdin and print to stdout
https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


pattern = r'^([4-6]\d{3}-?\d{4}-?\d{4}-?\d{4})$'
pattern_rep = r'(\d)\1\1\1'
valid = False
n = int(input())
for _ in range(n):
    credit = input()
    if re.match(pattern, credit) and len(re.findall(pattern_rep, credit.replace('-', ''))) == 0:  # noqa
        print('Valid')
    else:
        print('Invalid')

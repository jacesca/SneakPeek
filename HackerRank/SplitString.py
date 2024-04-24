"""
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
string s: the string to analyze
int k: the size of substrings to analyze

Example:
input:  'AABCAAADA'
Output:
AB
CA
AD
Note that a subsequence maintains the original order of
characters encountered. The order of characters in each
subsequence shown is important.
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
"""
from collections import Counter


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        print(''.join(dict(Counter(string[i:i+k])).keys()))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

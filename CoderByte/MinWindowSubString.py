"""
Min Window Substring

Have the function MinWindowSubstring(strArr) take the array of strings stored
in strArr, which will contain only two strings, the first parameter being the
string N and the second parameter being a string K of some characters, and your
goal is to determine the smallest substring of N that contains all the
characters in K.
For example:
if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that
contains the characters a, e, and d is "dae" located at the end of the string.
So for this example your program should return the string dae.
Another example:
if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that
contains all of the characters in K is "aabd" which is located at the
beginning of the string. Both parameters will be strings ranging in length from
1 to 50 characters and all of K's characters will exist somewhere in the string
N. Both strings will only contains lowercase alphabetic characters.

Examples:
Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje

Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
"""

from collections import Counter


def MinWindowSubstring(strArr):
    # code goes here
    n = strArr[0]
    k = strArr[1]

    # Counting occurences of k
    k_counter = Counter(k)
    w = []

    # # Option 1: Using for clauses
    # for l in range(len(k), len(n)+1):
    #   for i in range(len(n)):
    #     s = n[i:i+l]
    #     s_counter = Counter(s)
    #     if k_counter.keys() <= s_counter.keys():
    #       val_gte = all([k_counter[key] <= s_counter[key]
    #                      for key in k_counter.keys()])
    #       if val_gte:
    #         w.append(s)

    # # Option 2: Using list comprehension
    # w = [
    #   n[i:i+l]
    #   for l in range(len(k), len(n)+1)
    #   for i in range(len(n))
    #   if (k_counter.keys() <= Counter(n[i:i+l]).keys())
    # ]
    # w = [
    #   s for s in w
    #   if all([
    #     k_counter[key] <= Counter(s)[key]
    #     for key in k_counter.keys()
    #   ])
    # ]

    # Option 3: Simplifying the list comprehension
    w = [
        n[i:i+j]
        for j in range(len(k), len(n)+1)
        for i in range(len(n))
        if (k_counter.keys() <= Counter(n[i:i+j]).keys())
        and all([
            k_counter[key] <= Counter(n[i:i+j])[key]
            for key in k_counter.keys()
        ])
    ]
    return min(w, key=len)


# keep this function call here
cases = [
    ["aaabaaddae", "aed"],  # dae
    ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"],  # fafe
    ["caae", "cae"],  # caae
]
# print(MinWindowSubstring(input()))
for case in cases:
    print(MinWindowSubstring(case))

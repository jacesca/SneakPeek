#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    # Write your code here
    nums = [sum([arr[j] for j in range(5) if j != i]) for i in range(5)]
    print(min(nums), max(nums))


if __name__ == '__main__':
    # Example:
    # Input: 1 3 5 7 9
    # Output: 16, 24
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

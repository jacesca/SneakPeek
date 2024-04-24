"""
Given a square matrix, calculate the absolute difference between the sums
of its diagonals.

For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1 + 5 +9 = 15.
The right to left diagonal = 3 + 5 + 9 = 17.
Their absolute difference is |15 - 17| = 2.

Function description
Complete the  function in the editor below.
diagonalDifference takes the following parameter:
>> int arr[n][m]: an array of integers

Return
>>int: the absolute diagonal difference
"""
import os


def diagonalDifference(arr):
    # Write your code here
    x = sum([arr[i][i] for i in range(len(arr))])
    y = sum([arr[n-1-i][i] for i in range(len(arr))])
    return abs(x - y)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

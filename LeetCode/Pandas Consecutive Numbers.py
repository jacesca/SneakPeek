"""Consecutive Numbers
Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.

Find all numbers that appear at least three times consecutively.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears
consecutively for at least three times.
"""
import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    count, i = [], 0
    nums = logs.sort_values('id').num.values
    while i < len(nums) - 2:
        if nums[i] == nums[i+1] == nums[i+2]:
            if nums[i] not in count:
                count.append(nums[i])
            i += 3
        else:
            if i > 2 and nums[i-3] == nums[i-2] == nums[i-1] == nums[i]:
                i += 1 + (nums[i] == nums[i-1]) + (nums[i+1] == nums[i] == nums[i-1])  # noqa
            else:
                i += 1
    return pd.DataFrame({
        'ConsecutiveNums': count
    })


test_cases = [
    # pd.DataFrame({
    #     'id': [1, 2, 3],
    #     'num': [-1, -1, -1]
    # }),
    # pd.DataFrame({
    #     'id': [1, 2, 3, 4, 5, 6],
    #     'num': [9, 9, 9, 8, 8, 8]
    # }),
    # pd.DataFrame({
    #     'id': [1, 2, 4, 5, 6, 7],
    #     'num': [1, 1, 1, 1, 2, 1]
    # }),
    # pd.DataFrame({
    #     'id': [1, 2, 3, 4, 5],
    #     'num': [1, 1, 3, 3, 3]
    # }),
    pd.DataFrame({
        'id': [156, 157, 158, 159, 160, 162, 163, 165, 166, 168, 169,
               170, 171, 172, 174, 175, 177, 178, 180, 181, 183, 184, 186,
               187, 189, 190, 192, 193, 195, 196, 198, 199, 201, 202,
               204, 205, 207, 208, 210, 211, 212, 213],
        'num': [23, 23, 23, 33, 33, 47, 47, 32, 32, 27, 27,
                27, 25, 25, 41, 41, 36, 36, 38, 38, 4, 4, 17,
                17, 27, 27, 28, 28, 48, 48, 15, 15, 24, 24,
                12, 12, 35, 35, 38, 38, 38, 18]
    }),
]

for data in test_cases:
    print(consecutive_numbers(data))

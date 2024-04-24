"""Second Highest Salary
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+

id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Write a solution to find the second highest salary from the Employee
    table. If there is no second highest salary, return null (return None in
    Pandas). The result format is in the following example.
    """
    emp = employee.salary.sort_values(ascending=False).unique()
    # emp = employee.salary.unique().sort()[::-1]
    return pd.DataFrame({
        'SecondHighestSalary': [
            None if len(emp) < 2 else emp[1]
        ]
    })


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Write a solution to find the nth highest salary from
    the Employee table. If there is no nth highest salary, return null.
    """
    emp = employee.salary.sort_values(ascending=False).unique()
    return pd.DataFrame({
        f'getNthHighestSalary({N})': [
            None if len(emp) < N or N < 1 else emp[N-1]
        ]
    })


test_cases = [
    (pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]}), 2)
]

for data, n in test_cases:
    print(second_highest_salary(data))
    print(nth_highest_salary(data, n))
    print()

select name
from employee t1 join
(
select managerId from Employee
group by managerId
having count(managerId)>=5) as t2
on t1.id=t2.managerId

===========================

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee.groupby('managerId').size().reset_index(name="count")
    df=df[df['count']>=5]
    joined_table=pd.merge(df,employee,left_on='managerId', right_on='id', how='inner')
    return joined_table[['name']]

  
"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
"""

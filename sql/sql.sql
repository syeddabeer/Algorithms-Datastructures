Q.
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| Id          | int  |
| Salary      | int  |
+-------------+------+
Id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.

approach 1 without reporting null:
SELECT DISTINCT SALARY AS SecondHighestSalary
FROM EMPLOYEE
ORDER BY SALARY DESC
LIMIT 1 OFFSET 1

approach 2 for reporting null: MYSQL:
SELECT 
IFNULL (
(SELECT DISTINCT SALARY
FROM EMPLOYEE
ORDER BY SALARY DESC
LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary 



Q.
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| Id          | int  |
| Salary      | int  |
+-------------+------+
Id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.
 

Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

The query result format is in the following example.


approach 2:
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Set N = N-1;
RETURN (

SELECT 
IFNULL(
(SELECT DISTINCT SALARY
FROM EMPLOYEE
ORDER BY SALARY DESC
LIMIT 1 OFFSET N
), NULL) AS getNthHighestSalary

);
END


Q. SYNTAX OF FUNCTION?

CREATE FUNCTION NAME(N, INT) RETURNS INT
BEGIN
SET N=N-1
RETURN (




);
END




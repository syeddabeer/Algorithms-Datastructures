#Tag = Database

Q. Trial


CREATE TABLE EIMS
(
    issue_id VARCHAR(800),
    dis_txt VARCHAR(50)
    
);
INSERT INTO EIMS(issue_id, dis_txt)
VALUES  ('210921-126013','NFREE: 8492; 8493');

SELECT issue_id, Members.Member.value('.','VARCHAR(8000)') EIMS
FROM
(
 SELECT issue_id, CAST('<dis_txt><EIMS>'
        + REPLACE(dis_txt, '#' , '</EIMS><EIMS>') 
    + '</EIMS></dis_txt>' AS XML) AS tempTable 
 FROM ( 
   SELECT issue_id, TRANSLATE(dis_txt, ',;@', '###') AS dis_txt FROM EIMS
   ) AS temptable0
) AS tempTable
CROSS APPLY tempTable.nodes('/dis_txt/EIMS') Members(Member)


Q. 176. Second Highest Salary
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



Q. 177. Nth Highest Salary
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
+++++++++++++++++++++++++
CREATE FUNCTION NAME(N, INT) RETURNS INT
BEGIN
SET N=N-1
RETURN (




);
END


Q. 175. Combine Two Tables
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
This table contains information about the ID of some persons and their first and last names.
 

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
Each row of this table containts information about the city and state of one person with ID = PersonId.
 

Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a PersonId is not present in the Address table, report null instead.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Person table:
+----------+----------+-----------+
| PersonId | LastName | FirstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| AddressId | PersonId | City          | State      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| FirstName | LastName | City          | State    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the PersonId = 1 so we return null in their city and state.
AddressId = 1 contains information about the address of PersonId = 2.
++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++

SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p LEFT OUTER JOIN Address a
ON p.PersonId=a.PersonId


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++

Q. 181. Employees Earning More Than Their Managers
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Name        | varchar |
| Salary      | int     |
| ManagerId   | int     |
+-------------+---------+
Id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SELECT emp.Name AS Employee
FROM Employee emp INNER JOIN Employee mgr
ON emp.ManagerId=mgr.Id
WHERE emp.Salary>mgr.Salary



Q. 180. Consecutive Numbers

Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.
Write an SQL query to find all numbers that appear at least three times consecutively.
Return the result table in any order.
The query result format is in the following example.
Example 1:
Input: 
Logs table:
+----+-----+
| Id | Num |
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
Explanation: 1 is the only number that appears consecutively for at least three times.

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


SELECT DISTINCT l1.Num as ConsecutiveNums
FROM logs l1, logs l2, logs l3
WHERE
l1.Id = l2.Id-1 AND
l2.Id = l3.Id-1 AND
l1.Num = l2.Num AND
l2.Num = l3.Num

++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++

Q. 184. Department Highest Salary

Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key column for this table.
departmentId is a foreign key of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of a department and its name.
 

Write an SQL query to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++
# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e INNER JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId, salary) IN
(
    SELECT departmentId, Max(salary)
    FROM Employee
    GROUP BY departmentId
)

++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++


Q. 262. Trips and Users

Table: Trips

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | date     |     
+-------------+----------+
id is the primary key for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
 

Table: Users

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM type of ('Yes', 'No').
 

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
Output: 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
Explanation: 
On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50


++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


SELECT t.request_at as Day, 
        round(sum(case t.status when 'cancelled_by_driver' then 1 
                  when 'cancelled_by_client' then 1
                  else 0 end)/count(*), 2) as "Cancellation Rate" 
                  FROM Trips t 
                  WHERE '2013-10-01' <= t.Request_at and t.Request_at <= '2013-10-03' 
                  AND client_id IN (select users_id from Users where banned = 'No') 
                  AND driver_id IN (select users_id from Users where banned = 'No')
                  GROUP BY t.Request_at
++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q. 178. Rank Scores



Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

The query result format is in the following example.

 

Example 1:

Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' FROM Scores ORDER BY score DESC

++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q. 185. Department Top Three Salaries
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key column for this table.
departmentId is a foreign key of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of a department and its name.
 

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write an SQL query to find the employees who are high earners in each of the departments.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation: 
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++
SELECT d.name AS Department, a.name AS Employee, a.salary AS Salary 
FROM ( SELECT e.*, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS 'SalaryRank' FROM Employee e
) a INNER JOIN Department d
ON a.departmentId = d.id
WHERE SalaryRank <= 3;

++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q. 2004. The Number of Seniors and Juniors to Join the Company

Table: Candidates

+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| experience  | enum |
| salary      | int  |
+-------------+------+
employee_id is the primary key column for this table.
experience is an enum with one of the values ('Senior', 'Junior').
Each row of this table indicates the id of a candidate, their monthly salary, and their experience.
 

A company wants to hire new employees. The budget of the company for the salaries is $70000. The companys criteria for hiring are:

Hiring the largest number of seniors.
After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.
Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 20000  |
| 11          | Senior     | 20000  |
| 13          | Senior     | 50000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 2                   |
| Junior     | 2                   |
+------------+---------------------+
Explanation: 
We can hire 2 seniors with IDs (2, 11). Since the budget is $70000 and the sum of their salaries is $40000, we still have $30000 but they are not enough to hire the senior candidate with ID 13.
We can hire 2 juniors with IDs (1, 9). Since the remaining budget is $30000 and the sum of their salaries is $20000, we still have $10000 but they are not enough to hire the junior candidate with ID 4.
Example 2:

Input: 
Candidates table:
+-------------+------------+--------+
| employee_id | experience | salary |
+-------------+------------+--------+
| 1           | Junior     | 10000  |
| 9           | Junior     | 10000  |
| 2           | Senior     | 80000  |
| 11          | Senior     | 80000  |
| 13          | Senior     | 80000  |
| 4           | Junior     | 40000  |
+-------------+------------+--------+
Output: 
+------------+---------------------+
| experience | accepted_candidates |
+------------+---------------------+
| Senior     | 0                   |
| Junior     | 3                   |
+------------+---------------------+
Explanation: 
We cannot hire any seniors with the current budget as we need at least $80000 to hire one senior.
We can hire all three juniors with the remaining budget.


++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++
WITH cte AS
(SELECT *,
    SUM(salary) OVER (PARTITION BY experience ORDER BY salary) total_s
FROM Candidates)

SELECT experience, 
    SUM(IF(total_s<=70000, 1, 0)) accepted_candidates
FROM cte 
WHERE experience = 'Senior'
UNION
SELECT experience,
    SUM(IF(total_s<=70000-(SELECT IFNULL(MAX(total_s),0) FROM cte WHERE experience = 'Senior' AND total_s <= 70000), 1, 0)) accepted_candidates
FROM cte 
WHERE experience = 'Junior'

++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.197. Rising Temperature


Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature on a certain day.
 

Write an SQL query to find all dates Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++

SELECT Weather.id
FROM Weather 
JOIN Weather w
ON DATEDIFF(weather.recordDate, w.recordDate)=1
AND weather.temperature > w.temperature
++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q. 196. Delete Duplicate Emails

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++

DELETE p1 FROM Person p1, Person p2
WHERE
p1.Email = p2.Email AND p1.Id > p2.Id 



SELECT *
FROM Person
WHERE id NOT IN
(
SELECT p1.id
FROM Person p1, Person p2
WHERE p1.Email = p2.Email
AND p1.Id > p2.Id)
++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q. 1841. League Statistics

Table: Teams

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| team_id        | int     |
| team_name      | varchar |
+----------------+---------+
team_id is the primary key for this table.
Each row contains information about one team in the league.
 

Table: Matches

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| home_team_id    | int     |
| away_team_id    | int     |
| home_team_goals | int     |
| away_team_goals | int     |
+-----------------+---------+
(home_team_id, away_team_id) is the primary key for this table.
Each row contains information about one match.
home_team_goals is the number of goals scored by the home team.
away_team_goals is the number of goals scored by the away team.
The winner of the match is the team with the higher number of goals.
 

Write an SQL query to report the statistics of the league. The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points. If a match ends with a draw, both teams get one point.

Each row of the result table should contain:

team_name - The name of the team in the Teams table.
matches_played - The number of matches played as either a home or away team.
points - The total points the team has so far.
goal_for - The total number of goals scored by the team across all matches.
goal_against - The total number of goals scored by opponent teams against this team across all matches.
goal_diff - The result of goal_for - goal_against.
Return the result table ordered by points in descending order. If two or more teams have the same points, order them by goal_diff in descending order. If there is still a tie, order them by team_name in lexicographical order.

The query result format is in the following example.

++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++



Q.



++++++++++++++++++++++++++++ START ANSWER ++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++ END ANSWER ++++++++++++++++++++++++++++++++++++++++++




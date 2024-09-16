"""
Duplicate Emails

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.

"""

CREATE TABLE Person (
  id int,
  email varchar
  );

INSERT INTO Person (id, email)
VALUES 
('1','a@b.com'),
('2','c@d.com'),
('3','a@b.com')

method-1
=========
with cte as (
SELECT email, count(email) as number
From Person
group by email
  )
  select email from cte where number>=2


method-2
========
select email from Person
group by email
having count(email)>=2


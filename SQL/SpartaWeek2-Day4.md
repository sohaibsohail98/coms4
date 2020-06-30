# Week 2: 25/06: SQL Day 4:
Date functions:

- GETDATE - SELECT GETDATE() - To return the current date and time

- SYSDATETIME - SELECT SYSDATETIME() - To return the date and time of the computer being used

- DATEADD - DATEADD(d,5,Orderdate) AS “Due Date” - To add 5 days to the day.

It has 3 arguments: 
D or dd means day, m or mm month, yy or yyyy year
The date to be added to
How many units to add

- DATEDIFF - DATEDIFF(d,Orderdate,ShippedDate) AS “Ship Time” - To calculate difference between dates

- SELECT YEAR(OrderDate) AS “Order Year” - To extract the year from a date

- SELECT MONTH(OrderDate) AS “Order Month” - To extract the month from a date

- SELECT DAY(OrderDate) AS “Order Day” - To extract the day from a date.

- SUM - To add units, AVG - Working out the average, MAX - Working out the maximum value in the column. 

- HAVING is used instead of WHERE when filtering on subtotals/grouped data. 
Column Aliases can’t be used in the HAVING clause. 

- Logical (SYNTAX) Sequence:
- SELECT
DISTINCT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

- SQL Select Statement - Processing sequence:
FROM
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY

- Aggravated Functions with group by

SUM, COUNT, MAX, MIN, AVG to group the result-set by one or more columns.

- Group by - only works with related data. It’s a function to categorise the same values in the column. 

Join:

- SQL keyword - combine matched rows from two or more tables.

- inner join - which has the matching rows from both tables - in the combined table

- left join - everything from the left join and the matched rows from the right table 

- right join - everything from the right join and the matched rows from the left table 


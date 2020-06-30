# Week 2: 24/06: SQL Day 3:
ON DELETE CASCADE - Deleting all records related to the field, in the linked table and the original table.

SELECT * FROM table_name - means select all rows and columns from the table

SELECT row_name FROM table_name - specific row name presented from the table

SELECT * FROM Customers
WHERE City = ‘Paris’ - WHERE is for presenting the column heading and Paris is the actual value

SELECT COUNT(*) AS “Number of Employees in London” FROM Employees
WHERE City = ‘London’

- This is basically saying that how many employees are there that live in London from the ‘Employees’ table. 

When working with different columns (Aliasing):

SELECT c.CompanyName, c.City, c.Country, c.Region
FROM Customers c
WHERE c.Region=‘BC’

When you are selecting specific columns from a table and identifying a column’s particular field, you can name the table, to C.  

Select Top 10 values:

SELECT TOP 10 CompanyName, City
FROM Customers
WHERE Country=‘France’

Using AND or OR statements: 

SELECT p.ProductName, p.UnitPrice, p.CategoryID, p.Discontinued
FROM Products p
WHERE p.CategoryID = 1 OR p.Discontinued = 0

Using AND or OR statements with less than or more than symbols: 

SELECT p.ProductName, p.UnitPrice
FROM Products p
WHERE UnitsInStock > 0 AND UnitPrice > 29.99

Using DISTINCT statements: 

SELECT DISTINCT c.Country
FROM Customers c
WHERE ContactTitle = ‘Owner’

Distinct values ensures that you have no duplicate values and only one of the value.

Using Wildcards statements:

SELECT c.Country
FROM Customers c WHERE Country LIKE ‘U%’

This will get all the country statements beginning with ‘U’ which is like UK or USA. 

- The same way if you wanted to find values ENDING in a letter like ‘A’:

SELECT c.Country
FROM Customers c WHERE Country LIKE ‘%A’

- If you want to sort a value with more than one letter in the BEGINNING:

SELECT c.Country 
FROM Customers c WHERE Country LIKE ‘[UAM]%’

- The same way if you want to sort a value ENDING with more than one letter:

SELECT c.Country 
FROM Customers c WHERE Country LIKE ‘%[UAM]’

- You can also sort the results by alphabetical order or in the opposite alphabetical order:

It is also important to know that ORDER BY for ascending is by default so we do not input ASC.

SELECT c.Country 
FROM Customers c WHERE Country LIKE ‘%[UAM]’
ORDER BY c.Country DESC

SELECT c.Country 
FROM Customers c WHERE Country LIKE ‘%[UAM]’
ORDER BY c.Country 

- Values not starting with U or A or M:

SELECT c.Country 
FROM Customers c WHERE Country LIKE ‘[^UAM]%’

- Values which has the third letter as A

SELECT DISTINCT c.Country
FROM Customers c WHERE c.Country LIKE ‘__A%’

- Values which are only 2 characters and end in A and the first letter is anything:

SELECT * FROM Customers 
WHERE Region LIKE ‘_A’

- IN statements:

IN acts like equals but it can be done for multiple values:

SELECT * FROM Customers WHERE Region IN (‘WA’, ‘SP’)

- Another way to implement the IN statement without the IN:

SELECT * FROM Customers WHERE Region = ‘WA’ OR Region = ‘SP

SELECT * FROM Customers WHERE (Region = ‘WA’ OR Region = ‘SP) 
AND (Country=‘Brazil’ OR Country=‘USA’)

This is basically saying select the fields which regions are WA or SP and any of the two countries, Brazil or USA

- Below is another way of inputting this long command and the preferred method.

SELECT * FROM Customers WHERE Region IN(‘WA’,’SP’)
AND Country IN (‘Brazil’, ‘USA’)

- Values between and the actual two values:

SELECT * FROM EmployeeTerritories WHERE TerritoryID BETWEEN 06800 AND 09999

Identifying the territoryID between these two numbers and these two numbers too.

- What are the names and product IDs of the products with a unit price below 5.00?

SELECT p.ProductName, p.ProductID, p.UnitPrice 
FROM Products p WHERE p.UnitPrice<5.00

- Which categories have a category name with initials beginning with B or S

SELECT c.CategoryName, c.[Description]
FROM Categories c WHERE c.CategoryName LIKE ‘B%’ OR c.CategoryName LIKE ’S%’

- How many orders are there for EmployeeIDs 5 and 7 (The total for both)

SELECT * FROM Orders
WHERE EmployeeID IN (‘5’, ‘7’);

SELECT o.EmployeeID, COUNT (*) AS “Number of Employee orders with EmployeeIDs 5 and 7” 
FROM Orders o 
WHERE EmployeeID IN (‘5’, ‘7’)
GROUP BY o.EmployeeID

- Combining two fields together under one column and naming the column name:

SELECT c.CompanyName AS ‘Company Name’, c.City +’,’ + c.Country AS ‘City’
FROM Customers c

Shorter and another way to do it is:

SELECT c.CompanyName AS ‘Company Name’,
CONCAT(c.City, ‘, ‘,c.Country) AS “City”
FROM Customers c

-  Write a SELECT statement to list the six countries that have Region Codes in the customers Tables:

SELECT TOP 6 c.Country, c.Region 
FROM Customers c WHERE c.Region IS NOT NULL;

- Modulus - %: 
This means the remainder of the answer after division. 

76%3=1, 88/2=44, 90%7=6

- Round statement - rounding the decimal by 2

- String functions:

SUBSTRING:

SUBSTRING - SUBSTRING(expression, start, length)
SUBSTRING - SUBSTRING(name,1,1) for the initial

CHARINDEX:

CHARINDEX(‘a’, ‘text’) - this is to search for a string, for example: finding ‘a’ in a column called ‘text’ 

RIGHT or LEFT:

LEFT(name,5) for the first (or last) 5 characters 

LTRIM or RTRIM - Used to remove spaces for the beginning or end of a string.

LEN - LEN(name) - For the length of the name

REPLACE - REPLACE(name, ‘  ‘, ‘_’) - To replace spaces with underscores or any characters 

UPPER or LOWER - UPPER(name) - To convert to all upper (or lower) case. 




USE NORTHWIND

/*WHERE clause - filter the data*/
SELECT * FROM Customers
WHERE City = 'Paris'

1. SELECT COUNT(*) AS "Number of Employees in London" FROM Employees
WHERE City = 'London'

2. SELECT * FROM Employees
WHERE ContactTitle = 'Doctor'

3. SELECT * FROM Products
WHERE Discontinued

/* Getting table aliasing, and quickly identifying the columns */
SELECT c.CompanyName, c.City, c.Country, c.Region
FROM Customers c
WHERE c.Region='BC'

/* Selecting the top values*/
SELECT TOP 10 CompanyName, City
FROM Customers
WHERE Country='France'

SELECT COUNT(*) FROM Customers WHERE Country = 'France'

/* Using AND, you have to fulfull all the criteras need to be fulfilled. Using OR either of the criterias need to be fullied.*/

SELECT p.ProductName, p.UnitPrice, p.CategoryID, p.Discontinued
FROM Products p
WHERE p.CategoryID = 1 OR p.Discontinued = 0

SELECT p.ProductName, p.UnitPrice
FROM Products p
WHERE UnitsInStock > 0 AND UnitPrice > 29.99

SELECT DISTINCT c.Country
FROM Customers c
WHERE ContactTitle = 'Owner'

SELECT c.Country
FROM Customers c WHERE Country LIKE 'U%'

SELECT c.Country
FROM Customers c WHERE Country LIKE '%A'

SELECT c.Country 
FROM Customers c WHERE Country LIKE '[UAM]%'

SELECT c.Country 
FROM Customers c WHERE Country LIKE '%[UAM]'

SELECT DISTINCT c.Country
FROM Customers c WHERE c.Country LIKE '__A%'

SELECT DISTINCT p.ProductName
FROM Products p WHERE ProductName LIKE 'CH%'

SELECT * FROM Customers 
WHERE Region LIKE '_A'

SELECT * FROM Customers
WHERE Region IN ('WA', 'SP')

SELECT * FROM Customers WHERE Region = 'WA' OR Region = 'SP'

SELECT * FROM Customers WHERE (Region = ‘WA’ OR Region = ‘SP) 
AND (Country=‘Brazil’ OR Country=‘USA’)

SELECT * FROM Customers WHERE Region IN(‘WA’,’SP’)
AND Country IN (‘Brazil’, ‘USA’)

SELECT * FROM EmployeeTerritories WHERE TerritoryID BETWEEN 06800 AND 09999

--What are the names and product IDs of the products with a unit price below 5.00?--
1. SELECT p.ProductName, p.ProductID, p.UnitPrice 
FROM Products p WHERE p.UnitPrice<5.00

--Which categories have a category name with initials beginning with B or S--
2. SELECT c.CategoryName, c.[Description]
FROM Categories c WHERE c.CategoryName LIKE 'B%' OR c.CategoryName LIKE 'S%'

--How many orders are there for EmployeeIDs 5 and 7 (The total for both)--
3. SELECT * FROM Orders
WHERE EmployeeID IN ('5', '7');

SELECT o.EmployeeID, COUNT (*) AS "Number of Employee orders with EmployeeIDs 5 and 7" 
FROM Orders o 
WHERE EmployeeID IN ('5', '7')
GROUP BY o.EmployeeID

SELECT c.CompanyName AS 'Company Name', c.City +',' + c.Country AS 'City'
FROM Customers c

SELECT c.CompanyName AS 'Company Name',
CONCAT(c.City, ', ',c.Country) AS "City"
FROM Customers c

SELECT e.FirstName, e.LastName,
CONCAT (e.FirstName, ' ' , e.LastName) AS "Employee Name"
FROM Employees e

SELECT c.CompanyName AS 'Company Name', 
CONCAT (c.City, ', ' , c.Country) AS 'City'
From Customers c WHERE Region IS NULL

-- Write a SELECT statement to list the six countries that have Region Codes in the customers Tables--

SELECT TOP 6 c.Country, c.Region 
FROM Customers c WHERE c.Region IS NOT NULL;

SELECT UnitPrice, Quantity, Discount,
UnitPrice * Quantity AS "Gross Total"
From [Order Details]

SELECT od.UnitPrice, od.Quantity, od.Discount,
od.UnitPrice * od.Quantity AS "Gross Total",
ROUND((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.discount), 2)  AS "Net Total"
FROM [Order Details] od
ORDER BY "Gross Total" DESC

SELECT TOP 2 od.UnitPrice, od.Quantity, od.Discount,
od.UnitPrice * od.Quantity AS "Gross Total",
ROUND((od.UnitPrice * od.Quantity) - (od.UnitPrice * od.discount), 2)  AS "Net Total"
FROM [Order Details] od
ORDER BY "Net Total" DESC

--Changing column name to 'Post Code'

SELECT c.PostalCode "Post Code",
--Starts from the left, (CHARINDEX) looks for the space in the field and then it goes back one because of the -1--
LEFT(c.PostalCode, (CHARINDEX(' ',c.PostalCode))-1) AS "Post Code Region", 
CHARINDEX(' ',c.PostalCode) AS "Space Found", c.Country
FROM Customers c WHERE Country = 'UK'

SELECT p.productname "Product Names",
CHARINDEX ('''',p.ProductName) AS "Index of Quote"
FROM Products p
WHERE CHARINDEX('''',p.ProductName) > 0

/*STRING FUNCTIONS*/

CREATE TABLE film_table(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(50) NOT NULL,
    film_type VARCHAR(50)
)

INSERT INTO film_table VALUES
('    Star Wars', 'Sci fi'),
('Star Trek    ', 'Sci fi')

INSERT INTO film_table VALUES
('Batman', 'Action')


INSERT INTO film_table
(film_name) VALUES
('Superman')


SELECT * FROM film_table

SELECT * FROM film_table

SELECT film_name, CHARINDEX('a', film_name) AS "Position of Character" FROM film_table ;

SELECT film_name, SUBSTRING(film_name, 1, 3) AS "Extracted String" FROM film_table

SELECT film_name, RIGHT(film_name, 2) AS "Extracted String" FROM film_table

SELECT film_name, LEFT(film_name, 2) AS "Extracted String" FROM film_table

SELECT film_name, RTRIM(film_name) AS "Trimmed String" FROM film_table

SELECT film_name, LTRIM(film_name) AS "Trimmed String" FROM film_table

SELECT film_name, REPLACE(film_name,'M','A') AS "Replaced String" FROM film_table

SELECT film_name, LEN(film_name) AS "LENGTH of String" FROM film_table

SELECT film_name, UPPER(film_name) AS "Uppercase String", LOWER(film_name) AS "Lowercase String" FROM film_table

DROP TABLE film_table

--New Day--
USE Northwind

SELECT DATEADD(d,5,OrderDate) AS "Due Date"
FROM Orders
DATEDIFF(d,OrderDate, ShippedDate) AS "Ship Days";


SELECT 
CONCAT(e.FirstName, ' ', e.LastName) AS "Full name",
(DATEDIFF(DAY, e.BirthDate, GETDATE()) /365.25) AS "Their Current Age"
From Employees e

SELECT CASE 
WHEN DATEDIFF(d,OrderDate,ShippedDate) < 10 THEN 'On Time'
ELSE 'Overdue'
END AS "Status"
FROM Orders

SELECT CONCAT(e.Firstname, ' ', e.Lastname) AS "Name",
DATEDIFF (YY, BirthDate, GETDATE()) AS "Age",
CASE WHEN DATEDIFF(YEAR,BirthDate,GETDATE()) >= 65 THEN 'Retired'
WHEN DATEDIFF(YEAR,e.BirthDate, GETDATE()) >= 60 THEN 'Retirement Due'
ELSE 'MORE THAN 5 YEARS TO GO'
END AS "Retirement Status"
FROM Employees e

SELECT SUM(UnitsOnOrder) AS "Total On Order",
AVG(UnitsOnOrder) AS "Avg On Order",
MIN(UnitsOnOrder) AS "Min On Order",
MAX(UnitsOnOrder) AS "Max On Order"
FROM Products

SELECT * FROM Products

--Calculate Units On Order using aggregate functions per supplier--

SELECT SUM(p.UnitsOnOrder) AS "Total On Orders",
AVG(UnitsOnOrder) AS "Avg On Order",
MAX(UnitsOnOrder) AS "Max On Order"
FROM Products p
GROUP BY SupplierID

SELECT p.CategoryID,
AVG(p.ReorderLevel) AS "AVG Reorder Level"
FROM Products p
GROUP BY p.CategoryID,
ORDER BY "AVG Reorder Level" DESC

SELECT SupplierID, 
SUM(UnitsOnOrder) AS "Total On Order",
AVG(UnitsOnOrder) AS "Avg On Order",
FROM Products
GROUP BY SupplierID
HAVING AVG(UnitsOnOrder)>5

SELECT e.LastName, COUNT(o.OrderID) AS "NumberOfOrders" FROM (Orders INNER JOIN Employees e ON o.EmployeeID=e.EmployeeID)
GROUP BY LastName
HAVING COUNT(o.OrderID) > 10;

SELECT p.SupplierID,
AVG(p.UnitsOnOrder) AS "Average of the Units"
FROM Products p
GROUP BY p.SupplierID 

SELECT s.CompanyName AS "Supplier Name", AVG(p.UnitsOnOrder) AS "Average UnitsOnOrder"
FROM Products p
INNER JOIN Suppliers s
ON p.SupplierID=s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY "Average UnitsOnOrder" DESC

SELECT  s.CompanyName AS "Supplier Name", AVG(p.UnitsOnOrder) AS "Average UnitsOnOrder"
FROM products p
INNER JOIN Suppliers s ON p.SupplierID=s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY "Average UnitsOnOrder" DESC

--Homework--
SELECT
o.OrderID, o.OrderDate, o.Freight,
CONCAT (e.FirstName, ' ', e.LastName) AS "Employee name",
c.CompanyName AS "Company Name"
FROM Employees e INNER JOIN  orders o
ON o.customerID = c.CustomerID
INNER JOIN Customers c
ON o.EmployeeID = e.EmployeeID


SELECT OrderID, FORMAT(Orderdate, 'dd/MM/yyyy') AS "date"
FROM Orders; 

---Example of a sub-query---
SELECT Companyname AS "Customer"
FROM Customers c
WHERE c.CustomerID NOT IN (SELECT o.CustomerID FROM Orders o)

SELECT c.CompanyName AS "Customer"
FROM Customers c
LEFT JOIN Orders o ON o.CustomerID=c.CustomerID
WHERE o.CustomerID IS NULL

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
(SELECT MAX(od.UnitPrice) FROM [Order Details] od) AS "Max Price"
FROM [Order Details]

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount
FROM [Order Details]

SELECT od.ProductID, sq1.totalamt AS "Total Sold for this Product", od.UnitPrice, 
ROUND(((od.UnitPrice*od.Quantity)/sq1.totalamt)*100,2) AS "% of Total"
FROM [Order Details] od
INNER JOIN 
(SELECT ProductID, SUM (o.UnitPrice*o.Quantity) AS "totalamt"
FROM [Order Details] o
GROUP BY ProductID) sq1 ON sq1.ProductID=od.ProductID


--Activity--

SELECT od.OrderID, od.ProductID, od.UnitPrice, od.Quantity, od.Discount
FROM [Order Details] od
WHERE od.ProductID IN (SELECT p.ProductID FROM Products p WHERE p.Discontinued =1)

SELECT od.OrderID,od.ProductID,p.UnitPrice, od.Quantity, od.Discount
FROM [Order Details] od
INNER JOIN Products p
ON od.ProductID=p.ProductID
WHERE P.Discontinued = 1

SELECT e.EmployeeID AS "Employee/Supplier"
FROM Employees e
UNION ALL
SELECT s.SupplierID
FROM Suppliers s


SELECT * FROM PRODUCTS


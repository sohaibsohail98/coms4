/*1. Create a report showing the title of courtesy and the first and last name
of all employees whose title of courtesy is not "Ms." or "Mrs.".*/
SELECT * FROM Employees

SELECT e.TitleOfCourtesy
WHERE e.TitleOfCourtesy NOT LIKE 'Ms.' AND 'Mrs.' 
CONCAT (e.FirstName, ' ', e.LastName) AS "Employee name"
FROM Employees e

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName,
CONCAT(e.FirstName, ' ', e.LastName) AS "Employee name"
FROM Employees e
WHERE E.TitleOfCourtesy
NOT IN ('Ms.', 'Mrs.')


/*2. Create a report that shows the company name, contact title, city and country of all customers 
in Mexico or in any city in Spain except Madrid(in Spain).*/

SELECT c.CompanyName, c.ContactTitle, c.City, c.Country
FROM Customers c 
WHERE c.Country IN ('Mexico', 'Spain') AND c.city NOT IN ('Madrid')

/*3. Create a report showing the title of courtesy and the first and
last name of all employees whose title of courtesy begins with "M" and
is followed by any character and a period (.).*/
SELECT * FROM Employees

SELECT 
e.TitleOfCourtesy, e.FirstName, e.LastName
FROM Employees e 
WHERE e.TitleOfCourtesy LIKE ('M%.');

/*4. Create a report showing the first and last names of
all employees whose region is defined.*/

SELECT e.region, CONCAT (e.FirstName, ' ', e.LastName) AS 'The names of all employees'
FROM Employees e WHERE e.Region IS NOT NULL

/*5. Select the Title, FirstName and LastName columns from the Employees table.
  Sort first by Title in ascending order and then by LastName 
   in descending order.*/

SELECT e.Title, e.FirstName, e.LastName
FROM Employees e
GROUP BY e.lastname DESC
 



/*6. Write a query to get the number of employees with the same job title.*/


/*7.
Create a report showing the Order ID, the name of the company that placed the order,
and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required.
Sort by Company Name.
*/

/*8.
Create a report that shows the total quantity of per products (from the OrderDetails table) ordered. Only show records for products for which the quantity ordered is fewer than 200. 
The report should return*/



/*9.Create a report that shows the total number of orders by Customer since December 31, 1996. The report should only return rows for which the NumOrders is greater than 15. 
*/


/*10.  SQL statement will return all customers, and number of orders they might have placed. 
Include those customers as well who have not placed any orders.*/






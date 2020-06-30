# Week 2: 22/06: SQL: Day 1:

SELECT * - Displaying 

SP_HELP - Giving the structure of the table

Column - Database tables are composed of individual columns corresponding to the attributes of the object. 

Row - A row consists of one set of atttributes corresponding to one instance that a table describes. Also known as records or tuples. 

Table  - predefined format of rows  and columns - that define an entity. Known as a file. 

RDBMS - Relational Database management system - computer to perform database functions of storing, retrieving, adding, deleting and modifying data. 

Entity - anything that needs to be modelled (table)
It allows referencing what the table is about

Types of labels for data: Shop, time, date

Relational databases:

Primary key - unique and its own reference number, can’t be null value, it shouldn’t be changed - very less probability of change, can be auto-generated, each table have a maximum of one primary key

Foreign key - can have duplicate values, can be in multiple tables, can have null values. 

Types of database:

- Flat-file database: 
Stores everything in one table. Good for small numbers of records related to a single topic. 

- Relational database:
Gives you the ability to separate masses of data into numerous tables. 
Linked to each other through the use of keys - foreign and primary key

- Big data:
MonogoDB, Vertica, used for data analytics and business intelligence
Digital age and internet of things 

One to One relationship - Between two tables, referring to one record to another - One employee will only have one NHS ID. 

One to many relationship - one record from one table can be referred to more than one records from another table - one customer in relation to multiple purchase IDs. 

Many to many relationship - many records from one table be referred to many records from another table - many students in one table can be related to many course IDs from another table. 

Junction Table - When you need to establish a many-to-many relationship between two groups, the simplest solution is to use a Junction Table.

A Junction Table (sometimes referred to as a “Bridge Table”) is a table that contains references to both groups; bridging them together. (Example: Where there is a many to many relationship you can make a junction table with the primary keys of the tables, then form a junction table. This table then forms a composite primary key.

Composite primary keys -  combines more than one columns to make a unique value. 

Primary key candidates  - the potential for a record to be a primary key
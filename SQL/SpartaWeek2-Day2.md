# Week 2: 23/06: SQL: Day 2:
Structured query language:

Data manipulation language - DML - this is update the records:
- SELECT, INSERT, UPDATE, DELETE

Delete - inside the table, it uses the WHERE cause
SELECT - what columns you want to displayed
UPDATE - Updating a new row - something to add data to(Course name)
INSERT - inserting new rows into tables

DDL - Data definition language - this is for actual structure:
- CREATE, ALTER, DROP, TRUNCATE

CREATE - Creating a new structure
DROP - Dropping everything from the database
Alter - is adding a entire new column - a set of data, modify 
Truncate - removing the contents of the table but keeping the names of the rows.
Drop - completely drops the table from the database
Truncate - it deletes the data from the table, leaving an empty table.

DCL - Data control language (rights a user can have, decided by an administrator):
- GRANT - allowing particular fields to be changed and not other fields, REVOKE - removing privileges for users to edit, delete data.

TCL - Transaction control language
- COMMIT - apply the changes in the database, ROLLBACK - switch back to the original data, undo the changes committed, SAVEPOINT - saving the changes without showing it to everyone or updating the whole database

- CREATE - This allows you to create something, for example database

Data types used in SQL:

- VAR - stands for variable and its adaptable to different lengths of characters - records max size (letter, numbers, characters)
- CHAR - it is best to use for a fixed limit to characters, uses all of the characters assigned to it - it is much faster
- VARCHAR - variable length used - It only uses the characters assigned and the rest will be dropped - it is memory efficient (if in the brackets, it says 10 and we only use 5 characters, the rest will be dropped to save memory)  
- INT - it holds a integer value - 4bytes - the brackets will limit the number of characters
- DATE/TIME/DATETIME - storing date, time or both date and time
- DECIMAL or NUMERIC (p,s) - exact point-number, the p stands for precision is for the fixed length, the s is for scale which is the amount of characters after the decimal point. 
- BINARY - storing files/images
- FLOAT - scientific use for very large numbers
- BIT - used for a true or false value - boolean (0,1)


- Single quotes is used by VARCHAR, DATETIME, otherwise INT and DECIMAL values are without any quotes
- INT Identity (1,1) - Incremental value creating on its own - This means it starts from 1 and the second value is added to the first meaning 1+1=2 which means (1,2,3…..)  
- PRIMARY KEY - registering it as a primary key in the database
- If it’s separated from a comma, for example: PRIMARY KEY (director_id, director_number) - this is an example of a composite key
- NULL - means no value (undefined value)

Normalisation - better design, better use:

- 1st normal form:
ensuring redundant data is not placed in the database., no repeating groups, and each value is unique.

- 2nd normal form:
Making sure that the composite primary keys are interlinked and dependent on each other. All non-key attributes are fully functional dependent on the Primary key. 

- 3rd normal form:
There is no transitive functional dependency - make sure 

Constraints can be column level or table level.

**Some commonly used SQL constraints:**

NOT NULL - Ensures that a column cannot have a NULL value
DEFAULT - Sets a default value for a column when no value is specified.
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. It identifies each row in a table

DROP CONSTRAINT - it means dropping one of the rules imposed on the table or column.
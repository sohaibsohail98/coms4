USE Northwind

DROP DATABASE SOHAIB_SOHAIL_DATA

CREATE DATABASE SOHAIB_SOHAIL_DATA
USE SOHAIB_SOHAIL_DATA
CREATE TABLE my_favourite_films
(
    favourite_films VARCHAR(5),
    favourite_genre VARCHAR(5)
)
SP_HELP my_favourite_films

DROP TABLE my_favourite_films

DROP TABLE film_table
DROP TABLE director

CREATE TABLE film_table --This is to create a new table--
(
    film_name VARCHAR(10),
    film_type VARCHAR(8),
    release_date DATE,
    director VARCHAR(25),
    writer VARCHAR(25),
    star DECIMAL(2,1),
    film_lang CHAR(15),
    off_website VARCHAR(50),
    plot_summary VARCHAR(1000),
    film_id INT IDENTITY(1,1) PRIMARY KEY
)
INSERT INTO film_table --This is to insert rows into a table--
(   
    film_name, film_type, release_date, director, writer, star, film_lang, off_website, plot_summary
)
VALUES --This is to insert values into those rows.--
(
    'SQL', 'DRAMA', '2021/05/20', 'Sohaib Sohail', 'Christopher Nolan', 5.0, 'english', 'www.sql.com', 'amazing story line'
);

INSERT INTO film_table 
(   
    film_name, film_type, release_date, director, writer, star, film_lang, off_website, plot_summary
)
VALUES 

    ('L', 'MA', '2021/05/20', 'Sohaib Sohail', 'Christopher Nolan', 5.0, 'english', 'www.sql.com', 'amazing story line'),
    ('L', 'MA', '2021/05/20', 'Sohaib Sohail', 'Christopher Nolan', 5.0, 'english', 'www.sql.com', 'amazing story line')
;

SELECT * FROM film_table
SP_HELP film_table

CREATE TABLE director
(   
    director_id INT IDENTITY,
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'London',
    film_id INT,
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES film_table(film_id)
)

INSERT INTO director
(director_name, film_id)
VALUES
('David', 1)

INSERT INTO director
(director_name, film_id)
VALUES 
('Okla', 2)

SELECT * FROM director

DELETE FROM director WHERE film_id = 2
 
ALTER TABLE director
DROP CONSTRAINT film_id

ALTER TABLE director
ADD CONSTRAINT
FOREIGN KEY (film_id) 
REFERENCES film_table (film_id) ON DELETE CASCADE 


# README of CodiGo Backend
## Exercises from SQLBolt
- Exercise 1 : Statements
  ```
  SELECT * FROM movies;
  SELECT title FROM movies;
  SELECT title, year FROM movies;
  ```
- Exercise 2 : Statements
  ```
  SELECT * FROM movies where year between 2000 and 2010;
  SELECT title, year FROM movies limit 5;
  ```
- Exercise 3 : Statements
  ```
  SELECT * FROM movies where director not like 'John Lasseter';
  SELECT * FROM movies where title like 'WALL-%';
  ```
- Exercise 4 : Statements
  ```
  SELECT city, longitude FROM north_american_cities WHERE longitude < -87.629798 ORDER BY longitude ASC;
  SELECT * FROM north_american_cities where country='United States' order by population desc limit 2 offset 2;
  ```
- Exercise 5 : Statements
  ```
  SELECT id, title, domestic_sales, international_sales FROM movies inner join boxoffice on boxoffice.movie_id=movies.id
  where international_sales>domestic_sales;
  SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = building;
  ```

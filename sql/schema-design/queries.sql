-- Scenario 1
-- Retrieve the names of all gaming engines.
-- SELECT engine FROM gaming_engine;

-- Scenario 2
-- Find the total quantity of all games in stock.
-- SELECT COUNT(*) AS total_games FROM games;

-- Scenario 3
-- Get the unique titles of all games with a price higher than $30.00.
-- SELECT game_title, price FROM games WHERE price > 30.00;

-- Scenario 4
-- List the titles and quantities of games with less than 20 in stock.
-- SELECT game_title, quantity FROM games WHERE quantity < 20;

-- Scenario 5
-- Find the total number of genre-game associations.
-- SELECT COUNT(*) FROM game_genres;

-- Scenario 6
-- Retrieve the titles of action figures with a price between $20.00 and $50.00.
-- SELECT action_figure_title FROM action_figures WHERE price BETWEEN 20 AND 50;

-- Scenario 7
-- List the poster titles and prices for posters with quantities between 15 and 30.
-- SELECT poster_title, price FROM  posters WHERE quantity BETWEEN 15 AND 30;

-- Scenario 8
-- Get the names and positions of employees earning more than $40,000 per year.
-- SELECT employee_name, position FROM employees WHERE salary > 40000;

-- Scenario 9
-- Find the total number of social security entries.
-- SELECT COUNT(*) FROM social_security_employee;

-- Scenario 10
-- Retrieve the start and end times of all shifts.
-- SELECT start_time,end_time FROM shifts;

-- Scenario 11
-- Get the names and salaries of employees working on shifts.
-- SELECT shifts.start_time, shifts.end_time, employees.employee_name,employees.salary 
-- FROM shifts
-- JOIN employees ON shifts.employee_id=employees.employee_id;

-- Scenario 12
-- List the action figures with a quantity less than 15.
-- SELECT * FROM action_figures WHERE quantity < 15;

-- Scenario 13
-- Retrieve the titles of games with the word 'Warzone' in their title.
-- SELECT * FROM games WHERE game_title LIKE '%Warzone%';

-- Scenario 14
-- Find the total number of genres.
-- SELECT COUNT(*) FROM genres;

-- Scenario 15
-- Get the names and quantities of action figures with prices over $27.00.
-- SELECT action_figure_title, quantity FROM action_figures WHERE price > 27;

-- Scenario 16
-- Retrieve the names of employees in the 'IT Specialist' position.
-- SELECT employee_name FROM employees WHERE position = 'IT Specialist'

-- Scenario 17
-- List the game titles with quantities greater than 25.
-- SELECT game_title FROM games WHERE quantity > 25;

-- Scenario 18
-- Find the total quantity of all items (games, action figures, and posters).
-- SELECT SUM(total) FROM 
--     (
--     SELECT COUNT(*) AS total FROM games
--     UNION ALL
--     SELECT COUNT(*) AS total FROM action_figures
--     UNION ALL
--     SELECT COUNT(*) AS total FROM posters
--     ) AS total_quantity;

-- Scenario 19
-- Retrieve the social security numbers and names of employees with salaries over $50,000.
-- SELECT social_security_employee.ssn, employees.employee_name, employees.salary
-- FROM social_security_employee
-- JOIN employees ON social_security_employee.employee_id=employees.employee_id;

-- Scenario 20
-- Get the names and quantities of posters with prices between $10.00 and $15.00.
-- SELECT poster_title,quantity FROM posters WHERE price BETWEEN 10 AND 15;

-- Scenario 21
-- List the names and quantities of posters with a price less than $8.00.
-- SELECT poster_title,quantity FROM posters WHERE price < 8;

-- Scenario 22
-- Retrieve the employee names and salaries for 'Marketing Coordinator' and 'Finance Analyst' positions.
-- SELECT employee_name, salary FROM employees WHERE position IN ('Marketing Coordinator','Finance Analyst');

-- Scenario 23
-- Find the total quantity of action figures in stock.
-- SELECT SUM(quantity) FROM action_figures;

-- Scenario 24
-- Get the titles and quantities of games with a quantity between 15 and 30.
-- SELECT game_title,quantity FROM games WHERE quantity BETWEEN 15 AND 30;

-- Scenario 25
-- List the names and salaries of employees working on shifts with a start time after '2024-01-01'.
-- SELECT employees.employee_name,employees.salary, shifts.start_time
-- FROM employees
-- JOIN shifts ON shifts.employee_id=employees.employee_id AND shifts.start_time > '2024-01-01';

-- Scenario 26
-- Retrieve the titles and prices of games with prices less than $20.00.
-- SELECT game_title,price FROM games WHERE price < 20;

-- Scenario 27
-- Find the total quantity of action figures with prices between $25.00 and $30.00.
-- SELECT SUM(quantity) FROM action_figures WHERE price BETWEEN 25 AND 30;

-- Scenario 28
-- Get the names and positions of employees working on shifts with a start time before '2024-03-07 13:00:00'.
-- SELECT employees.employee_name,employees.position, shifts.start_time FROM employees
-- JOIN shifts ON shifts.employee_id=employees.employee_id AND shifts.start_time < '2024-03-07 13:00:00';


-- Scenario 29
-- List the names and quantities of action figures with a quantity greater than 10.
-- SELECT action_figure_title,quantity FROM action_figures WHERE quantity > 10;

-- Scenario 30
-- Retrieve the titles and quantities of posters with quantities greater than 25.
-- SELECT poster_title,quantity FROM posters WHERE quantity > 25;

-- Scenario 31
-- Find the total number of shifts.
-- SELECT COUNT(*) FROM shifts;

-- Scenario 32
-- Get the names and positions of employees working on shifts with a start time between '2024-02-01' and '2024-03-07 13:00:00'.
-- SELECT employees.employee_name,employees.position FROM employees
-- JOIN shifts ON shifts.employee_id=employees.employee_id WHERE shifts.start_time BETWEEN '2024-02-01' AND '2024-03-07 13:00:00';

-- Scenario 33
-- List the game titles with quantities less than 20.
-- SELECT game_title FROM games WHERE quantity < 20;

-- Scenario 34
-- Retrieve the names and quantities of action figures with prices over $23.00.
-- SELECT action_figure_title, quantity FROM action_figures WHERE price > 23;

-- Scenario 35
-- Find the total quantity of posters in stock.
-- SELECT SUM(quantity) FROM posters;

-- Happy querying!

-- Best regards, SQL Challenges Team
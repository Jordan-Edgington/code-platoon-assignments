DROP TABLE IF EXISTS posters CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS action_figures CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS gaming_engine CASCADE;
DROP TABLE IF EXISTS games CASCADE;
DROP TABLE IF EXISTS game_genres CASCADE;
DROP TABLE IF EXISTS social_security_employee CASCADE;
DROP TABLE IF EXISTS shifts CASCADE;

CREATE TABLE posters(
    poster_id BIGINT PRIMARY KEY,
    poster_title VARCHAR(50)
    UNIQUE NOT NULL
    CHECK (poster_title ~ '^[A-Z][A-Za-z0-9 -]+$'),
    quantity INT 
        NOT NULL
        CHECK(quantity > 0 AND quantity <= 30),
    price DECIMAL(4,2) 
        NOT NULL
        CHECK(price <= 20 AND price >= 6)
);

CREATE TABLE employees(
    employee_id BIGINT PRIMARY KEY,
    employee_name VARCHAR(40) 
        NOT NULL
        CHECK(employee_name ~ '^[A-Z][A-Za-z ]+$'),
    position VARCHAR(50) 
        NOT NULL
        CHECK(position IN (
            'Sales Associate',
            'Store Manager',
            'Inventory Clerk',
            'Customer Service Representative',
            'IT Specialist',
            'Marketing Coordinator',
            'Assistant Manager',
            'Finance Analyst',
            'Security Officer',
            'HR Coordinator'
            )),
    salary DECIMAL(7,2) 
        NOT NULL
        CHECK(salary > 31000.00 AND salary <= 65000)
        --real min should be 34652.80, but this fails based on the sample data, calculating salary on 40hrs/wk 52wks/yr
        --for now, writing as 31000.00
);


CREATE TABLE action_figures(
    action_figre_id BIGINT PRIMARY KEY,
    action_figure_title VARCHAR(50) 
        UNIQUE NOT NULL
        CHECK(action_figure_title ~ '^[A-Z][A-Za-z0-9 -]+$'),
    quantity INT 
        NOT NULL
        CHECK(quantity > 0),
    price DECIMAL(4,2) 
        NOT NULL
        CHECK(price > 10 AND price < 100)
);

CREATE TABLE genres(
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE gaming_engine(
    gaming_engine_id SERIAL PRIMARY KEY,
    engine VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE games(
    game_id INT PRIMARY KEY,
    engine_id INT,
    game_title VARCHAR(255) 
        UNIQUE NOT NULL
        CHECK (game_title ~ '^[A-Z][A-Za-z0-9 :\-\'']+$'),
                --first letter must be capitalized, rest of letters can be all of the rest including space colon hyphen and quote
    quantity INT 
        NOT NULL
        CHECK(quantity > 0),
    price DECIMAL(4,2) 
        NOT NULL
        CHECK(price > 10 AND price < 60),
    FOREIGN KEY (engine_id) REFERENCES gaming_engine(gaming_engine_id)
);

CREATE TABLE game_genres (
    id INT PRIMARY KEY,
    game_id INT,
    genre_id INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE social_security_employee(
    id SERIAL PRIMARY KEY,
    employee_id INT,
    ssn CHAR(11),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE shifts(
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

\COPY posters FROM './data/poster.csv' WITH CSV HEADER;
\COPY gaming_engine FROM './data/gaming_engine.csv' WITH CSV HEADER;
\COPY games FROM './data/game.csv' WITH CSV HEADER;
\COPY employees FROM './data/employee.csv' WITH CSV HEADER;
\COPY action_figures FROM './data/action_figure.csv' WITH CSV HEADER;
\COPY genres FROM './data/genre.csv' WITH CSV HEADER;
\COPY game_genres FROM './data/genre_game.csv' WITH CSV HEADER;
\COPY social_security_employee FROM './data/social_security.csv' WITH CSV HEADER;
\COPY shifts FROM './data/shifts.csv' WITH CSV HEADER;

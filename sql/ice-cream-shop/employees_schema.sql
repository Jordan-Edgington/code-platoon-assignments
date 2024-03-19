DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(40) NOT NULL,
    hours_per_week INT NOT NULL,
    role VARCHAR(20) NOT NULL
);

\COPY employees FROM './data/employees.csv' WITH CSV HEADER;
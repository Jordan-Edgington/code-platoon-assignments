DROP TABLE IF EXISTS sales;

CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(40) NOT NULL,
    quantity_of_cones INT NOT NULL,
    price DECIMAL(5,2) NOT NULL
);

\COPY sales FROM './data/sales.csv' WITH CSV HEADER;
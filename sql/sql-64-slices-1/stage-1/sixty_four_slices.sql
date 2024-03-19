DROP TABLE IF EXISTS stores;
CREATE TABLE stores(
    id SERIAL PRIMARY KEY,
    location VARCHAR(255) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS available_pizzas;
CREATE TABLE available_pizzas(
    id SERIAL PRIMARY KEY,
    name INT NOT NULL,
    price DECIMAL(2,4),
    store_id INT NOT NULL,
    FOREIGN KEY (store id) REFERENCES stores(id)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(20) NOT NULL,
    zip VARCHAR(20) NOT NULL,
    country VARCHAR(2),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
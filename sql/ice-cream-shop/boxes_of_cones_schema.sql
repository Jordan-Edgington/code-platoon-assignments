DROP TABLE IF EXISTS boxes_of_cones;

CREATE TABLE boxes_of_cones(
    id SERIAL PRIMARY KEY,
    type_of_cone VARCHAR(20) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(4,2) NOT NULL
);

\COPY boxes_of_cones FROM './data/boxes_of_cones.csv' WITH CSV HEADER;
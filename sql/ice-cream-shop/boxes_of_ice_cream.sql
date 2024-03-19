DROP TABLE IF EXISTS boxes_of_ice_cream;

CREATE TABLE boxes_of_ice_cream(
    id SERIAL PRIMARY KEY,
    type_of_ice_cream VARCHAR(30) NOT NULL,
    quantity INT NOT NULL
);

\COPY boxes_of_ice_cream FROM './data/boxes_of_ice_cream.csv' WITH CSV HEADER;
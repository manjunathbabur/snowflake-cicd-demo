USE WAREHOUSE your_warehouse;
USE DATABASE your_database;
USE SCHEMA your_schema;

CREATE OR REPLACE TABLE demo_table (
    id INT,
    name STRING
);

INSERT INTO demo_table (id, name) VALUES (1, 'Test');

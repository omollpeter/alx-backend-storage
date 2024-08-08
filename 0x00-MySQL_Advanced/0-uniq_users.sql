-- Creates a table users with three columns id, email and name
-- Should not fail even if the table exists

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

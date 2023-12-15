-- Creates a users table  with: (If table exists, script will not fail)
-- id, integer, primary key
-- email, string (255 characters), unique
-- name, string (255 characters)
-- can be executed on any database

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);

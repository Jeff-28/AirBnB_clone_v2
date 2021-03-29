-- A script that prepares a MySQL server for the project

-- Creates the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates the user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants privileges
GRANT SELECT ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

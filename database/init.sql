CREATE DATABASE persons;

USE persons;

CREATE TABLE person (
	PersonID int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	Firstname VARCHAR(30) NOT NULL,
	Lastname VARCHAR(50) NOT NULL
);
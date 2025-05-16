CREATE DATABASE animaldb;

/c animaldb

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(100),
    health VARCHAR(100)
);

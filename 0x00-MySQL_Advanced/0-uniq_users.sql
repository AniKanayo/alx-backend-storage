-- With the statement below we are ensuring that the table 'users' will only be created if it does not exist
CREATE TABLE IF NOT EXISTS users (
    -- Creating an 'id' column which will be an integer, can't be null, auto increments and is a Primary key
    id INT AUTO_INCREMENT,
    -- Creating an 'email' column which is a string of 255 max length, can't be null and should be unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Creating a 'name' column which is a string of 255 max length
    name VARCHAR(255),
    PRIMARY KEY (id)
) ENGINE=INNODB;

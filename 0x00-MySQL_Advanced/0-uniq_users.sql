--database selection, replace 'database_name' with your database
USE holberton;

-- table creation
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);

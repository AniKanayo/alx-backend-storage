-- Creating table 'users' only if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    -- Column 'id': integer, not null, auto increment, and primary key
    id INT AUTO_INCREMENT,

    -- Column 'email': string of 255 characters, cannot be null, and unique
    email VARCHAR(255) NOT NULL UNIQUE,

    -- Column 'name': string of 255 characters
    name VARCHAR(255),

    -- Column 'country': enumeration of countries (US, CO, TN), cannot be null, with a default of 'US'
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',

    PRIMARY KEY (id)
) ENGINE=INNODB;

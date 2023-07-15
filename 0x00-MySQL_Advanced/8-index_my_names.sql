-- Task: Create an index on the first letter of name in the names table

-- Import the names table
-- Unzip the names.sql.zip file and import it into the database using the mysql command-line tool

-- CREATE INDEX
ALTER TABLE names
ADD INDEX idx_name_first (name(1));

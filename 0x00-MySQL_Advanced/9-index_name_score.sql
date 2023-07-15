-- This SQL script does two things. First it adds a virtual
-- column that contains the first letter of each name in the names table.
-- Second it creates an index on that computed column and the score column.

ALTER TABLE names
ADD first_letter VARCHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) VIRTUAL;

CREATE INDEX idx_name_first_score
ON names (first_letter, score);

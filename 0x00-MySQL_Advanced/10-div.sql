-- This script creates a function that safely divides two numbers.
-- The function takes two arguments, a and b. If b is not equal to zero,
-- it returns the result of a divided by b. If b is zero, it returns 0.

DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //
DELIMITER ;

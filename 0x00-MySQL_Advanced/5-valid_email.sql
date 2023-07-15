DELIMITER //
-- Create a trigger that is activated before an update in the 'users' table
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users 
FOR EACH ROW
BEGIN
  -- If 'email' has been changed
  IF NEW.email <> OLD.email THEN
    -- Reset the 'valid_email' attribute
    SET NEW.valid_email = 0;
  END IF;
END; //
DELIMITER ;

DELIMITER //
-- Create the stored procedure 'AddBonus'
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  -- Declare a variable to store project id
  DECLARE project_id INT;

  -- Check if project exists
  SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- If project does not exists, create it
  IF project_id IS NULL THEN
    INSERT INTO projects(name) VALUES(project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Add the new correction
  INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
END; //
DELIMITER ;

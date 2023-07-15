-- This script creates a stored procedure that calculates
-- and stores the average score for a student specified by user_id.

DELIMITER // 

CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT) 
BEGIN
  -- Declare a variable to hold the average score.
  DECLARE averageScore DECIMAL(5, 2); 

  -- Calculate the average score for the specified user.
  SELECT AVG(score) INTO averageScore
  FROM corrections
  WHERE user_id = userId;

  -- Update the average score for the specified user in the users table.
  UPDATE users
  SET average_score = averageScore
  WHERE id = userId;
END //
DELIMITER ;

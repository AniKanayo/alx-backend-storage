-- Creates stored procedure ComputeAverageWeightedScoreForUser 
-- Which computes and stores the average weighted score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare a variable to store the average weighted score
    DECLARE avg_weighted_score DECIMAL(8,2);

    -- Compute the average weighted score
    SELECT 
        SUM(c.score * p.weight) / SUM(p.weight) INTO avg_weighted_score
    FROM corrections AS c
    JOIN projects AS p
    ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the user's average score
    UPDATE users 
    SET average_score = avg_weighted_score 
    WHERE id = user_id;
END //
DELIMITER ;

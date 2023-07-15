-- Compute and store the average weighted score for all students
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary table to store the computed average weighted scores
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_avg_scores (
        user_id INT,
        avg_score FLOAT
    );

    -- Compute the average weighted score for each student
    INSERT INTO temp_avg_scores (user_id, avg_score)
    SELECT 
        c.user_id,
        SUM(c.score * p.weight) / SUM(p.weight)
    FROM 
        corrections c 
    INNER JOIN 
        projects p ON c.project_id = p.id
    GROUP BY 
        c.user_id;

    -- Update the average_score field in the users table
    UPDATE 
        users u 
    INNER JOIN 
        temp_avg_scores t ON u.id = t.user_id
    SET 
        u.average_score = t.avg_score;

    -- Drop the temporary table
    DROP TABLE temp_avg_scores;
END$$

DELIMITER ;

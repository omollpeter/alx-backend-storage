-- This SQL script that creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE mean_score FLOAT;

    SELECT AVG(score) INTO mean_score FROM corrections WHERE user_id = in_user_id;
    UPDATE users SET average_score = mean_score WHERE id = in_user_id;
END //
DELIMITER ;

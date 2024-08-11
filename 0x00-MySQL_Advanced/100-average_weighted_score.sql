-- This SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DROP VIEW IF EXISTS user_view;

CREATE VIEW user_view
AS
SELECT corrections.user_id AS user, corrections.score AS score, projects.weight AS wgt
FROM corrections 
JOIN projects ON corrections.project_id = projects.id;


DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE mean_score FLOAT;
    DECLARE total_weight INT;
    -- DECLARE proj_id INT;

    SELECT SUM(weight) INTO total_weight FROM projects;
    SELECT SUM(score * wgt / total_weight) INTO mean_score FROM user_view WHERE user = in_user_id;
    UPDATE users SET average_score = mean_score WHERE id = in_user_id;
END //
DELIMITER ;

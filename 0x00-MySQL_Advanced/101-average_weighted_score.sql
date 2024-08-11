-- This SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DROP VIEW IF EXISTS user_view;

CREATE VIEW user_view
AS
SELECT corrections.user_id AS user, corrections.score AS score, projects.weight AS wgt
FROM corrections 
JOIN projects ON corrections.project_id = projects.id;


DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE current_id INT DEFAULT 1;
    DECLARE mean_score FLOAT;
    DECLARE total_weight INT;
    DECLARE all_ids INT;

    SELECT COUNT(id) INTO all_ids FROM users;

    WHILE current_id <= all_ids DO
        SELECT SUM(weight) INTO total_weight FROM projects;
        SELECT SUM(score * wgt / total_weight) INTO mean_score FROM user_view WHERE user = current_id;
        UPDATE users SET average_score = mean_score WHERE id = current_id;

        SET current_id = current_id + 1;
    END WHILE;
END //
DELIMITER ;

-- This SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE proj VARCHAR(255);
    DECLARE proj_id INT;
    SELECT name INTO proj FROM projects  WHERE name = project_name;
    IF (proj is NULL) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SELECT id INTO proj_id FROM projects WHERE name = project_name;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, proj_id, score);
END //
DELIMITER ;

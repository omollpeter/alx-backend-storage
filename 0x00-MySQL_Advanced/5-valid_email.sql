-- This SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed

DROP TRIGGER IF EXISTS check_valid_email;

DELIMITER //

CREATE TRIGGER check_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        IF NEW.email NOT LIKE "%_@%_.__%" OR "+" IN (NEW.email) THEN
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END //

DELIMITER ;

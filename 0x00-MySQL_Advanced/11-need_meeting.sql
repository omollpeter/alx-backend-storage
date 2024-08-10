 -- This is a SQL script that creates a view need_meeting that lists all students
-- Conditions score under 80 and last_meet null or more than month

CREATE VIEW need_meeting
 AS
 SELECT name
 FROM students
 WHERE score < 80 AND (last_meeting IS NULL OR DATEDIFF(CURDATE(), last_meeting) > 30);

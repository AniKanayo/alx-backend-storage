-- Creates a view need_meeting that lists all students that have a score under 80.
-- Also these students should either have no last meeting or had their last meeting more than one month ago.

CREATE VIEW need_meeting AS
SELECT *
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

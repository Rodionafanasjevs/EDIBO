# ADD NAME

CREATE DEFINER=`u05`@`%` PROCEDURE `testadd1`(IN p_name VARCHAR(20))
BEGIN INSERT INTO Timetable(name) VALUES(p_name);

END

CALL testadd1("Vasja");
select * from Timetable;

---

db05
DELIMITER $$
CREATE TRIGGER aizsargs BEFORE INSERT ON Tasks
FOR each ROW
BEGIN IF NEW.text="abc" THEN
SIGNAL SQLSTATE "50000" SET message_text = "Ai-jai-lai, kļuda!"

END;

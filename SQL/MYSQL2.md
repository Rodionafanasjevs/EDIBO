create table Test(id integer, title varchar(100));
insert into Test(id, title) values(1, "a");
insert into Test(id, title) values(2, "b");
insert into Test(id, title) values(3, "c");
select * from Test;

-- Your code here!

DELIMITER $$
CREATE FUNCTION ManaFunkcija (solis int)
RETURNS INT

BEGIN
   DECLARE lielums, done INT;
   DECLARE mainig1 integer;
   DECLARE mainig2 varchar(10);

   DECLARE cursors_ikesh_tabulas CURSOR FOR SELECT id, title FROM Test;
   --SET done = FALSE;
   --OPEN cursors_ieksh_tabulas;
--   lasiishanas_cikls: LOOP
--         FETCH cursors_ieksh_tabulas INTO mainig1, mainig2;
--         lielums = lielums + mainig1;
--         IF done THEN
--           LEAVE lasiishanas_cikls;
--         END IF;
--     END LOOP;
--     CLOSE cursors_ieksh_tabulas;
   
   

   SET lielums = 0;

  label1: WHILE lielums <= 100 DO
     SET lielums = lielums + solis;
  END WHILE label1;

   RETURN lielums;

END; $$

DELIMITER ;

SELECT '------';

INSERT INTO Test(title) VALUES (ManaFunkcija(3));
SELECT * FROM Test;

 

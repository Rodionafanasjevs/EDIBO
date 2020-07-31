use db05

CREATE TABLE Test(id integer, title varchar(100));
insert into Test(id,title) values(1, "Hello");
select * from Test;

DECLARE stuff INT;
SET stuff == Select ManaFunkcija(1);

DELIMITER $$
CREATE FUNCTION ManaFunkcija ( solis INT )
RETURNS INT

BEGIN
	DECLARE lielums INT;
    
    SET lielums = 0;
    
    DECLARE cursors_leksh_tabulas CURSOR FOR SELECT * FROM TEST;
    DECLARE done int default false;
    DECLARE mainig1 integer;
    DECLARE mainig2 varchar(10);
    OPEN cursors_leksh_tabulas: LOOP
		FETCH cursors_leksh_tabulas INTO mainig1. mainig2;
        
        IF done TRUE
			LEAVE read_loop;
		END IF;
	END LOOP;
    CLOSE cursor_l;
        
    
    label1: WHILE lielyms <= 50 DO
		SET lielums = lielums + solis;
	END WHILE label1;
    
    RETURN lielums;
    
END; $$

DELIMITER;

SELECT '.....';

INSERT INTO Test(title) Values (ManaFunkcija(5));
SELECT * FROM Test;

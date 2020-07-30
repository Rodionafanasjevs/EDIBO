mysql -h database-1.cxnurhwpmz0x.eu-central-1.rds.amazonaws.com -u u05 -P 3000 -p
USE

db05

mysql> CREATE TABLE Timetable(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),lastname VARCHAR(20),age INT NOT NULL DEFAULT 420,date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

mysql> ALTER TABLE Timetable ADD day VARCHAR(20) ;

mysql> SELECT * from Timetable;

mysql> INSERT INTO Timetable(name,lastname,age,day)VALUES("Rich","Upitis",24,"Pirmdiena")

mysql> UPDATE Timetable SET name="Kiril",lastname="Boblick" WHERE id=1;

mysql> UPDATE Timetable SET age=31,day="Otrdiena" WHERE id=1;

mysql> INSERT INTO Timetable(name,lastname,age,day)VALUES("Ron","Baronis",24,"Otrdiena");

mysql> INSERT INTO Timetable(name,lastname,age,day)VALUES("Janis","Kanolis",39,"Trešdiena");

mysql> INSERT INTO Timetable(name,lastname,age,day)VALUES("Aleksandrs","Usik",33,"Piektina");

mysql> INSERT INTO Timetable(name,lastname,age,day)VALUES("Ralf","Netorks",39,"Ceturtdina");

---

# HELP

CREATE TABLE ediboKG5(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),lastname VARCHAR(20),age INT NOT NULL DEFAULT 420,date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

ALTER TABLE ediboKG ADD age INT NOT NULL; - add a column to a table

UPDATE edibo SET location = "USA" WHERE name = "Donald" - updates tables location for Donald

ALTER TABLE edibo MODIFY location VARCHAR(20) NOT NULL DEFAULT "Riga";

INSERT INTO ediboKG3(name,lastname,age,date) VALUES("Kriss","G",69,now());

SELECT DATE_FORMAT(date, "%d/%m/%Y") FROM ediboKG3;

SELECT age as "kaut kads numurs",date as datums FROM ediboKG3;

select name as Vards,age as Vecums,date as Datums from ediboKG3 WHERE name = "Kriss";

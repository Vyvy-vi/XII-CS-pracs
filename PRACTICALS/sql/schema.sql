CREATE DATABASE IF NOT EXISTS cs_practicals;
USE cs_practicals;

CREATE TABLE IF NOT EXISTS BUS(
    BusNo INT PRIMARY KEY,
    Origin VARCHAR(100),
    Dest VARCHAR(100),
    Rate INT,
    Km INT
);

INSERT INTO BUS
    SELECT 0, 'Delhi', 'Noida', 150, 10
        FROM DUAL
        WHERE NOT EXISTS (SELECT BusNo FROM BUS WHERE BUS.BusNo = 0);
INSERT INTO BUS
    SELECT 1, 'Goa', 'Chennai', 15000, 50
        FROM DUAL
        WHERE NOT EXISTS (SELECT BusNo FROM BUS WHERE BUS.BusNo = 1);

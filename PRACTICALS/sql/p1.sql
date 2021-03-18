/*part i*/
SELECT Watch_Name, Qty_Sold FROM WATCHES W, SALES S WHERE W.WatchId = S.WatchId AND S.Quarter = 1;
/*part ii */
SELECT * FROM WATCHES WHERE Watch_Name LIKE ‘%Time’;
/* part ii*/
SELECT SUM(Qty_Store) FROM WATCHES WHERE Type LIKE ‘Unisex’;
/* part iv*/
SELECT Watch_Name, Price FROM WATCHES WHERE Price BETWEEN 5000 AND 15000;
/* part v*/
SELECT WatchId, SUM(Qty_Sold) FROM SALE GROUP BY WatchId;


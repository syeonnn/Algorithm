-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN,'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE 
WHERE SUBSTR(ADDRESS,1,3)="경기도"
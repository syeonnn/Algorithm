-- 코드를 입력하세요
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE*BS.SALES) AS TOTAL_SALES
FROM BOOK B 
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE like '2022-01-%'
GROUP BY AUTHOR_ID, CATEGORY 
ORDER BY AUTHOR_ID, CATEGORY desc
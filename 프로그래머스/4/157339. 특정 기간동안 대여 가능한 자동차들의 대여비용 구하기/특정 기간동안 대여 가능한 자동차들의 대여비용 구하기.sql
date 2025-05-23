SELECT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE*(1-D.DISCOUNT_RATE/100)*30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D ON C.CAR_TYPE = D.CAR_TYPE

WHERE C.CAR_TYPE IN ('세단', 'SUV') AND D.DURATION_TYPE like '30%'
AND C.CAR_ID NOT IN (
    SELECT CAR_ID 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01' 
)
GROUP BY CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC
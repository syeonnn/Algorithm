WITH REST AS (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES, RANK() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RNK
    FROM REST_INFO 
)

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST
WHERE RNK = 1
ORDER BY FOOD_TYPE DESC

WITH ED AS (
    SELECT ID, RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS RNK
    FROM ECOLI_DATA
)

SELECT ID, (
    CASE
    WHEN RNK <= (SELECT COUNT(*) FROM ECOLI_DATA) * 1/4 THEN 'CRITICAL'
    WHEN RNK <= (SELECT COUNT(*) FROM ECOLI_DATA)  * 2/4 THEN 'HIGH'
    WHEN RNK <= (SELECT COUNT(*) FROM ECOLI_DATA)  * 3/4 THEN 'MEDIUM'
    ELSE 'LOW' END ) AS COLONY_NAME
FROM ED
ORDER BY 1
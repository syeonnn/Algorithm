-- 코드를 입력하세요
SET @HOUR = 8;
SELECT (@HOUR := @HOUR + 1) HOUR, (SELECT COUNT(*) 
                                   FROM ANIMAL_OUTS 
                                   WHERE HOUR(DATETIME) = @HOUR
                                  ) COUNT
FROM ANIMAL_OUTS 
WHERE @HOUR < 19
ORDER BY HOUR;
SELECT COUNT(ID) AS FISH_COUNT, MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH(TIME)
ORDER BY MONTH
# 월은 숫자형태 (1~12) 로 출력
# 9 이하의 숫자는 두 자리로 출력하지 않음
# 잡은 물고기가 없는 월은 출력하지 않음
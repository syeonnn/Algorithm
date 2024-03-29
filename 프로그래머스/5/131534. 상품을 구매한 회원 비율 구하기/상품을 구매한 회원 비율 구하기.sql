SELECT A.YEAR AS YEAR, -- 연도
       A.MONTH AS MONTH, -- 달
       COUNT(*) AS PUCHASED_USERS,
       -- USER_INFO 테이블에 있고, 등록한 연도가 2021인 모든 행을 센다.(= 2021년에 가입한 모든 회원)
       -- COUNT(*) : 해당 FROM에 있는 행의 개수를 모두 센다(즉, ONLINE으로 2021년에 구매한 회원의 정보를 조회해서 행을 카운트)
       -- 다시말해서, 2021년에 구매한 회원수/2021년에 가입한 모든 회원 수 => 2021년 구매한 회원 비율 (소수점 2자리수에서 반올림)
	   ROUND((COUNT(*)/ (SELECT COUNT(*) 
                            FROM USER_INFO 
                         WHERE YEAR(JOINED) = 2021)), 1) AS PUCHASED_RATIO
FROM ( -- 두테이블을 조합하여 새로운 테이블 만든다.
    SELECT DISTINCT -- YEAR, MONTH, USER_ID 조합이 중복이 없도록
        YEAR(S.SALES_DATE) AS YEAR, -- 연도만 따로 뺀다
        MONTH(S.SALES_DATE) AS MONTH,-- 월만 따로 뺀다
        U.USER_ID
    FROM ONLINE_SALE S
    JOIN USER_INFO U 
        ON S.USER_ID = U.USER_ID -- USER_ID기준으로 JOIN(연결)
        AND YEAR(U.JOINED) = 2021 -- 가입한 년도가 2021년 이고
) A

GROUP BY A.YEAR, A.MONTH -- 연도, 달의 두개 그룹화한다.
ORDER BY A.YEAR, A.MONTH
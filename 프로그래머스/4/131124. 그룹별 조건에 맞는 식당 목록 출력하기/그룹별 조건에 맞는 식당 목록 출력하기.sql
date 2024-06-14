-- 리뷰를 가장 많이 작성한 회원의 리뷰들
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M JOIN REST_REVIEW R
ON M.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID # GROUP BY 절 이용해 데이터를 그룹화해야 함
    ORDER BY COUNT(MEMBER_ID) DESC # 집계함수 쓰려면 
    LIMIT 1
)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT
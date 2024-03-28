-- 코드를 작성해주세요
SELECT II.ITEM_ID, II.ITEM_NAME, II.RARITY
FROM ITEM_INFO AS II INNER JOIN ITEM_TREE AS IT
ON II.ITEM_ID = IT.ITEM_ID
WHERE II.ITEM_ID NOT IN (SELECT PARENT_ITEM_ID 
                         FROM ITEM_TREE 
                         WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC
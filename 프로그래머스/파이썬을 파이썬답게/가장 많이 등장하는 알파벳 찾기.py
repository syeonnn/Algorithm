# 문제 설명
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

# 제한 조건
# mystr의 원소는 알파벳 소문자로만 주어집니다.
# mystr의 길이는 1 이상 100 이하입니다.

from collections import Counter

my_str = input().strip()
original = Counter(my_str)
values = [v for v in Counter(my_str).values()]
values.sort(reverse = True)
biggest = values[0]

result = [k for k,v in original.items() if biggest == v]
result = ''.join(sorted(result))

print(result)

# 3       
# KOREAKOREAKOREAKOREAKOREAKOREA
# SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY 

T = int(input())
for t in range(1, T + 1):

    sen = input()

    for i in range(10):
        if sen[:i] == sen[i:i*2]:
            print(f'#{t} {i}')
            break

# 공포도가 x인 모험가는 x명 이상으로 여행을 떠나야 함
# 최대 몇 개의 모험가 그룹을 만들수 있을 것인가?
# (이때 남는 모험가가 있어도 괜찮다)

import sys
read = sys.stdin.readline

n = int(read())
fear = list(map(int, read().split()))
fear.sort()
cnt, ans = 0, 0

for i in fear:
    cnt+=1
    if cnt>=i:
        ans+=1
        cnt = 0

print(ans)
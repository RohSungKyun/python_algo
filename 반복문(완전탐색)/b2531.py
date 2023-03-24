# 회전 초밥
# 1. k번 연속으로 초밥을 먹을시 할인 2. 특정 번호의 쿠폰을 하나 발행하여 무료로 제공한다. 3. 최대한 다양한 종류의 초밥을 먹으려 한다.

import sys
read = sys.stdin.readline

N, d, k, c = map(int, read().split())
array = [0]*N

for i in range(N):
    array[i] = int(read())

MaxCount = 0
for i in range(N):  
    tmp = set()
    index=i  
    for j in range(k):
        if index > N-1: # 인덱스 초과
            tmp.add(array[index%N-1])
            index+=1
        else:
            tmp.add(array[index])
            index+=1

    if c not in tmp:
        count = len(set(tmp))+1
        if count>MaxCount:
            MaxCount = count
    else:
        count=len(set(tmp))
        if count>MaxCount:
            MaxCount = count
print(MaxCount)
    

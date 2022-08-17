# 회의실 배정 문제

import sys
read = sys.stdin.readline

n = int(read())
arr=[]
cnt=0
end=0

for i in range(1, n+1):
    arr.append(list(map(int, read().split()))) # 시작과 종료시간을 묶어서 저장
print(arr)

# 오름차순 정렬을 수행해야 정답으로 인정된다.(테스트 케이스에는 정렬이 이루어져 있지 않기 때문이다.)
arr.sort(key = lambda x : x[0])
arr.sort(key = lambda x : x[1])

print(arr)
for a, b in arr: # 시작, 끝
    if a >= end: # 이전 끝 시간보다 크거나 같다면 
        cnt+=1
        end = b

print(cnt)
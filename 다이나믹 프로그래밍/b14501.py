# 퇴사
# 기간에 따라 상담을 건너뛸 필요가 있다. n 기간 안에서만 이루어 져야 한다.


import sys
read = sys.stdin.readline

n = int(read())
arr = []

for i in range(n):
    t, p = map(int, read().split())
    arr.append([t, p])

# 최대 이익 이므로 가격을 테이블에 저장
dp = [0]*16


for i in range(1, n+1):
    for j in range(i+arr[i][0], n+1):
        if j < n:
            



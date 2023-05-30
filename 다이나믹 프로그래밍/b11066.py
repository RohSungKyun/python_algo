# 파일 합치기
# 파일을 합칠 때 발생하는 비용을 최소로 만드는 결과
# **누적합 개념 필요**

import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):

    k = int(read()) # 장의 개수
    arr = list(map(int, read().split()))

    
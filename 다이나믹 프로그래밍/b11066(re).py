# 파일 합치기
# 파일을 합칠 때 발생하는 비용을 최소로 만드는 결과
# **누적합 개념 필요**

import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):

    k = int(read()) # 장의 개수
    arr = list(map(int, read().split()))
    dp = [[0]*(k+1) for _ in range(k+1)]
    prefix_sum = []
    for i in range(1, k+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    for i in range(2, k+1): # 합치는 파일의 길이
        for j in range(1, k+2-i): # 구간합의 시작점
            dp[j][j+i-1] = min(dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)) + (prefix_sum[j+i-1] - prefix_sum[j-1])
    
    print(dp[1][n])
    
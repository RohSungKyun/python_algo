import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    dp = [[0]*(n) for _ in range(2)]

    arr = [list(map(int, read().split())) for _ in range(2)]


    # Need to make exceptions when length is 1 and 2
    # If the length is 1
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # if the length is 2
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
    
    # init dp table 
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]
    for i in range(2, n):
        for j in range(2):

            # the maximum value two spaces before
            dp[j][i] = max(dp[0][i-2], dp[1][i-2]) + arr[j][i]
            # the maximum value one sapce before
            dp[j][i] = max(dp[j][i], dp[(j+1)%2][i-1] + arr[j][i])
    print(max(dp[0][-1], dp[1][-1]))
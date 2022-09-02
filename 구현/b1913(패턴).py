import sys
read = sys.stdin.readline
n = int(read())
target = int(read())
arr = [[0]*n for i in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx=0
x = y = n//2
cnt = num = 2

while True:
    for _ in range(4):
        px, py = dx[idx], dy[idx]
        for _ in range(cnt):
            x+=px
            y+=py
        
            arr[x][y] = num
            if num==target:
                tx=x
                ty=y
            if num==n**2:
                break
            num+=1
        idx = (idx+1)%4
    cnt+=2
    x-=1
    y-=1
for i in arr:
    print(*i)
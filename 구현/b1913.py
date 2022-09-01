import sys
read = sys.stdin.readline
n = int(read())
target=int(read())
arr = [[-1]*n for i in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cl = n**2
x, y = 0, 0
idx=0

while cl>0:
    arr[x][y] = cl
    if cl==target:
        tx, ty = x, y
    
    nx, ny = x+dx[idx], y+dy[idx]
    if 0<=nx<n and 0<=ny<n and arr[nx][ny] == -1:
        x, y = nx, ny
        cl-=1
    else:
        idx = (idx+1)%4
    
for i in arr:
    print(*i)
    
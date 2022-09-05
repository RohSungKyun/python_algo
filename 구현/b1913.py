import sys
# 무식하게 겉에서 채우는 방식
read = sys.stdin.readline

n = int(read())
target = int(read())

arr = [[-1]*n for i in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cx, cy = 0, 0
cur_num = n*n

idx=0

while cur_num>1 and n>=3 and n<=999:
    if cur_num == target:
        tx, ty = cx+1, cy+1 # idx가 아니라 좌표이므로 +1을 해준다.
        

    arr[cx][cy] = cur_num # cx, cy에 변화를 준다.
    nx = cx+dx[idx]
    ny = cy+dy[idx]
    if 0<=nx<n and 0<=ny<n and arr[nx][ny] == -1:
        cx, cy = nx, ny
        cur_num -= 1
    else:
        idx = (idx+1)%4
arr[cx][cy] = cur_num
for i in arr:
    print(*i)
print(tx, ty)
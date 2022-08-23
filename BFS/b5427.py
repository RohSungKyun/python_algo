import sys
from collections import deque
read = sys.stdin.readline
# 필요한 조건 : 해당 칸이 이동 가능한지, 방문한 적이 없는지, 불이 붙지 않았는지 => 3번째 조건을 위해 불의 시간을 따로 구해야 함

n = int(read())

for _ in range(n):
    w, h = map(int, read().split())
    fire = [[0]*w for i in range(h)]
    people = [[0]*w for i in range(h)]
    arr = [[0]*w for i in range(h)]
    queue = deque()
    dx=[-1, 0, 1, 0]
    dy=[0, -1, 0, 1]
    for i in range(h):
        str = read().rstrip()
        idx=0 # 해당 가로줄의 인덱스
        for j in str: # 이동 가능 여부 체크
            if j == '@':
                px = i
                py = idx
                arr[i][idx] = 1
            if j == '.':
                arr[i][idx] = 1
            if j == '*':
                queue.append([i, idx])
                fire[i][idx] = 1
                arr[i][idx] = 1
            idx+=1

    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and arr[nx][ny]==1 and fire[nx][ny]==0:
                fire[nx][ny] = fire[x][y] + 1
                queue.append([nx, ny])
    queue.append([px, py])
    people[px][py] = 1
    ans = 987654321
    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 and nx>w-1 and ny<0 and ny>h-1:
                ans = min(ans, people[x][y]+1)
                continue
            if (arr[nx][ny] == 1 and people[nx][ny] == 0 and fire[nx][ny] == 0 or fire[nx][ny] > people[x][y]+1): # 방문한 적이 없고, 이동가능하며(arr=1), 불의 위치
                people[nx][ny] = people[x][y] + 1
                queue.append([nx, ny])
    if ans == 987654321:
        print("IMPOSSIBLE")
    else:
        print(ans-1)
    
            


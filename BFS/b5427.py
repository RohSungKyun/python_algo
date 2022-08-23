import sys
from collections import deque
read = sys.stdin.readline
# 필요한 조건 : 해당 칸이 이동 가능한지, 방문한 적이 없는지, 불이 붙지 않았는지 => 3번째 조건을 위해 불의 시간을 따로 구해야 함
n = int(read())
for i in range(n):
    w, h = map(int, read().split())
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    queue = deque()
    arr_p = [[0]*w for _ in range(h)] # 사람의 소요시간
    fire = [[0]*w for _ in range(h)] # 불의 소요시간
    arr = [[0]*w for _ in range(h)]
    for x in range(h): # 몇번째 높이인지
        str = read().rstrip()
        idx=0 # 해당 줄에서 몇번째 위치인지 즉 arr[x][idx]
        for tmp in str:
            if tmp == '.':
                arr[x][idx] = 1 # 이동 가능
            if tmp == '@':# 사람의 위치인 경우
                arr[x][idx] = 1 # 이동가능
                px = x
                py = idx # 해당 위치를 기록
            if tmp == '*': #불의 위치인 경우
                arr[x][idx] = 1 # 불이 이동가능
                fire[x][idx] = 1 # 불의 위치 체크
                queue.append([x, idx]) # 불의 소요시간 계산을 먼저하기위해 넣어둠
            idx+=1
    while (len(queue)!=0):
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx >= h or ny >= w: # x축은 몇번째 줄, y 축은 해당 줄의 몇번째 그러므로 x:h, y:w
                continue
            if arr[nx][ny]==1 and fire[nx][ny]==0: # 이동가능하며 방문한 적이 없다면
                fire[nx][ny] = fire[x][y] + 1
                queue.append([nx, ny])

    queue.append([px, py]) # 사람의 bfs시작
    arr_p[px][py] = 1
    ans = sys.maxsize
    while (len(queue)!=0):
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx >= h or ny >= w: # 범위 밖 즉 탈출했을 경우 소요시간
                ans = min(ans, arr_p[x][y]+1)
                continue
            if arr_p[nx][ny] == 0 and arr[nx][ny] == 1 and fire[nx][ny] == 0 or fire[nx][ny] > arr_p[x][y] + 1:
                arr_p[nx][ny] = arr_p[x][y] + 1
                queue.append([nx, ny])
    if ans == sys.maxsize:
        print("IMPOSSIBLE")
    else:
        print(ans-1)

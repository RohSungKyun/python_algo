# n x n 복도
# 선생님(장애물뒤에있는 학생은 발견x 그외 4가지 직선 방향은 모두 파악 가능), 학생, 장애물
# 장애물은 추가로 3개 설치할 수 있다.
import sys
from itertools import combinations
read = sys.stdin.readline

n = int(read())
graph = []
teachers = []
spaces = []

for i in range(n):
    graph.append(list(map(str, read().split())))
    for j in range(n):
        if graph[i][j]=='T':
            teachers.append((i, j))
        if graph[i][j]=='X':
            spaces.append((i, j))
            
# 감시 함수
def watch(x, y, direction):
    # 왼쪽방향으로 감시
    if direction == 0:
        while y>=0: # 가로축이다.
            if graph[x][y]=='S':
                return True
            if graph[x][y]=='O':
                return False
            y-=1
    # 오른쪽 방향으로 감시
    if direction==1:
        while y<n:
            if graph[x][y]=='S':
                return True   
            if graph[x][y]=='O':
                return False
        y+=1
    # 위쪽 방향으로 감시
    if direction==2:
        while x>=0:
            if graph[x][y]=='S':
                return True   
            if graph[x][y]=='O':
                return False
        x-=1
    # 아래쪽 방향으로 감시
    if direction==3:
        while x<n:
            if graph[x][y]=='S':
                return True   
            if graph[x][y]=='O':
                return False
        x+=1
    return False

# 장애물 설치후 학생감지 함수
def process():
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

result = False
# 빈 공간에 3개의 장애물을 채우는 모든 경우의 수
for d in combinations(spaces, 3):
    # 장애물 설치
    for x, y in d:
        graph[x][y]='O'
    if not process():
        result = True
        break
    for x, y in d:
        graph[x][y] = 'X' # 장애물을 다시 제거

if result:
    print('YES')
else:
    print('NO')
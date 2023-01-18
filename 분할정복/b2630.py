import sys
read = sys.stdin.readline
# 파란색 :1, 하얀색:0, 분할정복, 재귀
n = int(read())
cp = []
for i in range(n):
    cp.append(list(map(int, read().split())))

def solve(nbs, x, y):
    global blue, white
    if nbs == 1: # 분할하여 나온 값이 1일 경우 더해줌
        if cp[x][y]==1:
            blue+=1
            return
        else:
            white+=1
            return

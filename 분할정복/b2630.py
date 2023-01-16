import sys
read = sys.stdin.readline
# 파란색 :1, 하얀색:0, 분할정복, 재귀
n = int(read())
cp = []
for i in range(n):
    cp.append(list(map(int, read().split())))


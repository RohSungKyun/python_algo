import sys
read = sys.stdin.readline
t = int(read())
# 빨강, 초록, 파랑으로 칠하는 비용
rgb = []
for i in range(t):
    rgb.append(list(map(int, read().split())))

for i in range(1, t):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2])+rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2])+rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1])+rgb[i][2]

print(min(rgb[t-1]))
import sys
read = sys.stdin.readline

n = int(read())
dots = [[0]*2 for _ in range(n)]

for i in range(n): # 순서쌍을 이중 배열에 저장
    d, c = map(int, read().split())
    dots[i][0], dots[i][1] = d, c

distance = [0]*n

# 각 점의 모든 최소거리를 저장하는 브루트포스 방식이 필요(현재 위치를 제외한 모든 점과 비교해야 함)
for i in range(n):
    for j in range(n):
        if dots[i][1] == dots[j][1] and i!=j: # 같은 색일 경우
            dist = abs(dots[i][0] - dots[j][0])
            if distance[i] == 0:
                distance[i] = dist

            if distance[i] !=0 and distance[i]>dist:
                distance[i] = dist
                
td = 0
for i in distance:
    td+=i
print(td)
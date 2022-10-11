import sys
read = sys.stdin.readline

n = int(read())


graph = [0]
graph.append(list(map(int, read().split()))) # 처음은 계산할 필요가 없다.

for i in range(2, n+1):
    graph.append(list(map(int, read().split())))
    for j in range(i):
        if j == 0 :
            graph[i][j] = graph[i-1][j] + graph[i][j] # 이전 왼쪽 끝 + 현재 왼쪽 끝
        elif j == i-1:
            graph[i][j] = graph[i-1][j-1] + graph[i][j] # 이전 오른쪽 끝 + //
        else:
            graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j] # 둘 중 큰 값 가져오기

print(max(graph[n]))
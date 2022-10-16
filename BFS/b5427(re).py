from collections import deque

for _ in range(int(input())):
    W, H = map(int, input().split())
    visited_S = [[0] * W for _ in range(H)]
    visited_F = [[0] * W for _ in range(H)]
    graph = []
    queue_S = deque()
    queue_F = deque()
    flag = 0
    for h in range(H):
        graph.append(list(input()))
        for w in range(W):
            if graph[h][w] == '@':
                graph[h][w] = '.'
                queue_S.append((h, w))
                visited_S[h][w] = 1
                if h == 0 or h == H - 1 or w == 0 or w == W - 1:
                    flag = 1
            if graph[h][w] == '*':
                queue_F.append((h, w))
                visited_F[h][w] = 1

    if flag:
        print(1)
        continue

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        while queue_F:
            x, y = queue_F.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited_F[nx][ny] and graph[nx][ny] == '.':
                        visited_F[nx][ny] = visited_F[x][y] + 1
                        queue_F.append((nx, ny))

        while queue_S:
            x, y = queue_S.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited_S[nx][ny] and graph[nx][ny] == '.':
                        if visited_F[nx][ny] == 0 or visited_S[x][y] + 1 < visited_F[nx][ny]:
                            visited_S[nx][ny] = visited_S[x][y] + 1
                            queue_S.append((nx, ny))
                            if nx == 0 or ny == 0 or nx == H - 1 or ny == W - 1:
                                return visited_S[nx][ny]
        return 'IMPOSSIBLE'

    print(bfs())

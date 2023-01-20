from collections import deque

# N x M 개수 입력
n, m = map(int, input().split())


# N x M 2차원 리스트 입력
graph = []
for i in range(n):
    # 띄어쓰기 없이 입력
    graph.append(list(map(int, input())))


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 로 노드 방문
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 갈 수 없는 길인 경우
            if graph[nx][ny] == 0:
                continue

            # 방문하지 않은 노드인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))
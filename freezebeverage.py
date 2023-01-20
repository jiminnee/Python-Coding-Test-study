# 음료수 얼려 먹기 문제 (DFS)

# N x M 개수 입력
n, m = map(int, input().split())

# N x M 2차원 리스트 입력
graph = []
for i in range(n):
    # 띄어쓰기 없이 입력
    graph.append(list(map(int, input())))

# DFS 로 노드 방문
def dfs(x,y):

    # 그래프 벗어나는 경우 종료
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return False

    # 방문하지 않은 인접 노드 방문
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False


# 만들 수 있는 아이스크림 개수 세기
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)
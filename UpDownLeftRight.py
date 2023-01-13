# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# 이동 방향 리스트
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

# 이동 방향 차례로 확인
for plan in plans :

    # L, R, U, D 차례로 확인
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        # 맵을 벗어난 경우 무시
    if nx < 1 or ny <1 or nx >n or ny >n :
        continue

    x,y = nx, ny

print(x,y)
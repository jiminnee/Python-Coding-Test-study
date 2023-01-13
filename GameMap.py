# 말의 현재 위치 입력받기
location = input()

# 행
row = int(location[1])

# 열
column = int(ord(location[0])) - int(ord('a')) + 1

# 말이 갈 수 있는 위치
goto = [(1,2), (2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
count = 0

# 갈 수 있는 위치 확인
for go in goto :
    next_row = row + go[0]
    next_column = column + go[1]

    # 말이 갈 수 있는 경우
    if next_row >= 1 and next_column >=1 and next_row <= 8 and next_column <= 8 :
        count += 1

print(count)

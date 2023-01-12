n = 1260
count = 0

# 큰 단위의 화폐부터 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:

    # 해당 화폐로 거슬러 줄 수 있는 개수
    count += n // coin

    # 남은 금액
    n %= coin

print(count)
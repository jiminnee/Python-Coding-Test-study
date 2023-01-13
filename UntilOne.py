# N , K 입력 받기
n, k = map(int, input().split())
count = 0

# k 이상일 때
while n >= k :
    # k 로 나누어 떨어질 때
    if n % k == 0 :
        n //= k
        count += 1
    else :
        n -= 1
        count += 1

# k 보다 작을 때는, 단순히 1 빼기
while 1 < n < k:
    n -= 1
    count += 1

print(count)


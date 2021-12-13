# 방법1
n = 25
k = 3

count = 0

while True:
    # n % k == 0일 때까지 n-1을하면서 카운트 1 증가시키기
    if n % k != 0:
        n -= 1
        count += 1
    # n // k 을 n에 적용하면서 카운트 1 증가시키기
    else:
        n //= k
        count += 1
    # 만약 n=1이면 중단
    if n == 1:
        break
print(count)

# 방법2
# n,k를 공백을 기준으로 구분하여 입력받기
n, k = map(int,input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
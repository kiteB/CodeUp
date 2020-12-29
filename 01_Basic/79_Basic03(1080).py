# 1, 2, 3, ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수 (0~1000)보다 같거나 작을 때까지 계속 더하기
a = int(input())
s = 0

for i in range(1, a+1):
    s += i
    if s >= a:
        print(i)
        break
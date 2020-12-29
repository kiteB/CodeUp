# 1부터 n까지 정수를 순서대로 계속 더해나갈 때,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하고, 합을 출력하기
a = int(input())
s = 0

for i in range(1, a+1):
    s += i
    if s >= a:
        print(s)
        break;

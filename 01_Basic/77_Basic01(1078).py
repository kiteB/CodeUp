# 정수 (1~100) 1개를 입력받아 1부터 그 수까지 짝수 합을 구하기
a = int(input())
s = 0

for i in range(1, a+1):
    if i % 2 == 0:
        s += i
print(s)
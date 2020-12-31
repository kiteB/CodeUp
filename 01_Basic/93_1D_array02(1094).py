# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력하기
n = int(input())
a = input().split()

numbers = []

for i in range(0, n):
    numbers.append(int(a[i]))

for i in range(n-1, -1, -1):
    print(numbers[i], end=' ')
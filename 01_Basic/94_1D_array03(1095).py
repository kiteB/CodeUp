# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호 출력하기
n = int(input())
a = input().split()

min = int(a[0])
for i in range(1, n):
    if min > int(a[i]):
        min = int(a[i])
    else:
        i += 1

print(min)
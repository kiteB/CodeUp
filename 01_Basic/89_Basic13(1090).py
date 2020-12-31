# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램 만들기
a, r, n = map(int, input().split())

for i in range(n-1):
    a = a * r

print(a)

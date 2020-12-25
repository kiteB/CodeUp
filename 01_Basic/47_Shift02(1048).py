# 정수 2개 (a, b)를 입력받아 a를 2^b배 곱한 값으로 출력하기
# Ex) 1 3이 입력되면 1을 2^3(8)배하여 출력하기
a, b = map(int, input().split())
print(a<<b)
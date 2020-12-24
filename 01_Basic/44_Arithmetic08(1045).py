# 정수 2개 (a,b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산하기
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('%.2f' %(a/b))
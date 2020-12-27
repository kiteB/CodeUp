# 입력된 두 정수 a,b 중 큰 값을 출력하기
# 단, 조건문을 사용하지 않고 3항 연산자 ? 사용하기
# python은 ? 연산자가 없음 -> (a if 조건 else b)를 사용함.

a, b = map(int, input().split())
print(a if a>b else b)
# 입력된 세 정수 a,b,c 즁 가장 작은 값을 출력하기
# 단, 조건문을 사용하지 않고 3항 연산자 ? 사용하기
# python은 ? 연산자가 없음 -> (a if 조건 else b)를 사용함.
a, b, c = map(int, input().split())
num = (a if a<b else b)
print(num if num<c else c)
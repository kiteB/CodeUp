# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참 출력
a, b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)
result = int(not b1) and int(not b2)
# 두 가지의 참(1) 또는 거짓(0)이 입력될 때,참/거짓이 서로 다를 때에만 참을 출력
a, b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)
print((a ^ b))
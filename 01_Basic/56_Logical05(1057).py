# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참
a, b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)
b_xor = b1 ^ b2
print(int(not(b_xor)))
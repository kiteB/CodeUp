# 두 개의 참(1) 또는 거짓(0)이 입력될 때,하나라도 참이면 참을 출력
a, b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)
print(int(b1 or b2))
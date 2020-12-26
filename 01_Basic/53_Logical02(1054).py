# 두 개의 참(1) 또는 거짓(0)이 입력될 때,모두 참일 때에만 참을 출력
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
result = int(a and b)
print(result)
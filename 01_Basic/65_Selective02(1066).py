# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd) 출력하기
a = map(int, input().split())
for i in a:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd) 출력하기
a = int(input())

if a > 0:
    print('plus')
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
else:
    print('minus')
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
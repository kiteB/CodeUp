# 3 6 9 게임 만들기
# 10보다 작은 정수 1개가 입력될 때,
# 1부터 그 수까지 순서대로 공백을 두고 수를 출력하고,
# 3 또는 6 또는 9인 경우에는 그 수 대신 영문 대문자 X 출력하기
a = int(input())

for i in range(1, a+1):
    if i == 3 or i == 6 or i == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')

# 정수가 순서대로 입력될 때 (-2147483648 ~ +2147483647, 단 개수는 알 수 없음)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단시키기
a = input().split()

for i in a:
    if int(i) == 0:
        break
    else:
        print(i)
# 'q'가 입력될 때까지 입력한 문자를 계속 출력하기
a = input().split()

for i in a:
    print(i)
    if i == 'q':
        break

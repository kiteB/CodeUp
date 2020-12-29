# A,B,C,D,E,F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용 출력하기
a = int(input(), 16)

for i in range(16):
    print(('%X' %a) + '*' + ('%X' %i) + '=' + ('%X' %(a*i)))

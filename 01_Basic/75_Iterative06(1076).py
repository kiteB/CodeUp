# 영문자 (a~z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력하기
# Ex) f 입력 -> a b c d e f 출력
x = input()
alpha = ord(x)
start = ord('a')

while start <= alpha:
     print(chr(start), end=' ')
     start += 1
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는 방문 주기가 공백을 두고 입력될 때,
# 3명이 다시 모두 함께 문제를 풀어보는 날(동시 가입/ 동업 후 며칠 후)을 출력하기
a, b, c = map(int, input().split())
day = 1

while (day % a != 0) or (day % b != 0) or (day % c != 0):
    day += 1

print(day)
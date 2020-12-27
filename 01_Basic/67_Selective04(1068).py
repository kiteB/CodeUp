# 점수(정수, 0~100)를 입력받아 평가를 출력하기
# 90 이상: A, 70 이상: B, 40 이상: C, 40 미만: D
score = int(input())

if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 40:
    print('C')
else:
    print('D')
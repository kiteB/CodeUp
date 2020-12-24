# 정수 3개를 입력받아 합과 평균을 출력하기
a, b, c = map(int, input().split())
sum = a+b+c
print(sum)
print('%.1f' %(sum/3))
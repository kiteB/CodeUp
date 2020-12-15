# 연월일 입력받아 그대로 출력하기
# Ex) 2013.8.5를 입력받았을 때 2013.08.05 형식으로 출력하기
year, month, day = input().split('.')
print(year.zfill(4), month.zfill(2), day.zfill(2), sep='.')
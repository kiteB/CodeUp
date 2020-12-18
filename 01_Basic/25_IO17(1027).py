# 년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력하기
year, month, day = input().split('.')
print(day.zfill(2), month.zfill(2), year.zfill(4), sep="-")
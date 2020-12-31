# 출석 번호를 n번 무작위로 불렀을 때,
# 각 번호(1~23)가 불린 횟수를 각각 출력하기
n = int(input())
a = input().split()

numbers = [0 for i in range(23)] # 모든 요소를 0으로 초기화

for i in range(n):
    numbers[int(a[i])-1] += 193

for i in range(0, 23):
    print(numbers[i], end=' ')
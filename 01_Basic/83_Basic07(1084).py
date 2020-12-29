# r,g,b 각각의 빛의 개수가 주어질 때,
# (빛의 강약에 따라 0 ~ n-1까지의 n 가지의 빛 색깔을 만들 수 있다.)
# 주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓수 계산하기
r, g, b = map(int, input().split())
count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1

print(count)


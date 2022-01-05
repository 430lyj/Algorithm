def solution(n, rgb):
    temp = rgb[0]
    for price in rgb[1:]:
        price[0] += min(temp[1], temp[2])
        price[1] += min(temp[0], temp[2])
        price[2] += min(temp[1], temp[0])
        temp = price
    return min(rgb[-1])

n = int(input())
rgb = []
for i in range(n):
    temp = list(map(int, input().split(' ')))
    rgb.append(temp)
print(solution(n, rgb))

import math
def solution(r, b, m):
    count = 0
    while b > 0:
        interest = b * (r/100)
        if (interest * 1000) // 10 >= 5:
            interest = math.ceil(interest * 100) / 100
        else:
            interest = math.floor(interest * 100) / 100
        b += interest
        
        b -= m
        count += 1
        if count > 1200:
            return "impossible"
    return count

n = int(input())
answer = []
for i in range(n):
    r, b, m = tuple(map(float, input().split()))
    print(solution(r, b, m))
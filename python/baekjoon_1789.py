def solution(n):
    number, total = 0, 0
    while total < n:
        total += number
        number += 1
    if total > n:
        return number - 2
    return number - 1

n = int(input())
print(solution(n))
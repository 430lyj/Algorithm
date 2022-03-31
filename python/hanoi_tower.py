answer = []

def hanoi_tower(n, start, mid, target):
    global answer
    if n == 1:
        answer += [[start, target]]
    else:
        hanoi_tower(n-1, start, target, mid)
        answer.append([start, target])
        hanoi_tower(n-1, mid, start, target)

def solution(n):
    hanoi_tower(n, 1, 2, 3)
    return answer
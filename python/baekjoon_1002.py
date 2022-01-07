import math

def solution(cho, baek):
    distance = math.sqrt((cho[0] - baek[0])**2 + (cho[1]-baek[1])**2)
    if distance == 0:
        if cho[2] == baek[2]: return -1
        return 0
    if (distance == cho[2] + baek[2]) or (distance == abs(cho[2] - baek[2])):
        return 1
    elif distance < cho[2] + baek[2] and distance > abs(cho[2] - baek[2]):
        return 2
    else:
        return 0

n = int(input())
answer = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    cho, baek = (temp[0], temp[1], temp[2]), (temp[3], temp[4], temp[5])
    answer.append(solution(cho, baek))

for ans in answer:
    print(ans)
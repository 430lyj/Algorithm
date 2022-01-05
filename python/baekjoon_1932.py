def solution(n, tri):
    temp = tri[0]
    for line in tri[1:]:
        for i in range(len(line)):
            line[i] += max(temp[i], temp[i+1])
        temp = line
    return tri[-1][0]

n = int(input())
tri = []
for i in range(n):
    temp = list(map(int, input().split(' ')))
    tri.append(temp)

tri.reverse()
print(solution(n, tri))
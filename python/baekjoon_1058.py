import sys

n = int(input())
graph_list = [list(input()) for _ in range(n)]
graph_link = []
for graph in graph_list:
    temp = []
    for i in range(n):
        if graph[i] == 'Y':
            temp.append(i)
    graph_link.append(temp)
print(graph_link)
answer = []

stack = []
visited = [0] * n
for i in range(n):
    count = 0
    visited = [0] * n
    for j in graph_link[i]:
        stack.append((i, j))
    while stack:
        x, y = stack.pop()
        visited[y] = 1
        count += 1
        for point in graph_link[y]:
            print(point)
            if visited[point] == 0:
                stack.append((y, point))
    answer.append(count)

print(*answer)
print(max(answer))

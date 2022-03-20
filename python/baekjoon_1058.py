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
answer = []

visited = [0] * n
for i in range(n):
    count = 0
    stack = []
    visited = [0] * n
    visited[i] = 1
    for j in graph_link[i]: # 1차 친구들만 카운트
        stack.append(j) 
        visited[j] = 1
        count += 1
    for l in stack:
        for k in graph_link[l]:
            if visited[k] != 1:
                visited[k] = 1
                count += 1
    answer.append(count)

print(max(answer))
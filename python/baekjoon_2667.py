from collections import deque
n = int(input())
house = [list(map(int, input())) for _ in range(n)]

# to_be_visited = deque()
# visited = [[0] * n for _ in range(n)] # 0은 not visited / 1은 visited

# ans = []
# danji_cnt, cnt = 0, 0
# x, y = 0, 0
# while visited != house:
#     cnt = 0
#     print(x, y, house[x][y])
#     if house[x][y] == 1 and visited[x][y] == 0:
#         to_be_visited.append((x, y))
#         danji_cnt += 1
#     while to_be_visited: #bfs
#         x, y = to_be_visited.popleft()
#         if house[x][y] == 1 and visited[x][y] == 0:
#             cnt += 1
#             visited[x][y] = 1
#         else:
#             x, y = to_be_visited.popleft()
#         if x < n - 1 and house[x+1][y] == 1 and visited[x+1][y] == 0:
#             to_be_visited.append((x+1, y))
#         if y < n - 1 and house[x][y+1] == 1 and visited[x][y+1] == 0:
#             to_be_visited.append((x, y+1))
#         if x > 0 and house[x-1][y] == 1 and visited[x-1][y] == 0:
#             to_be_visited.append((x-1, y))
#         if y > 0 and house[x][y-1] == 1 and visited[x][y-1] == 0:
#             to_be_visited.append((x, y-1))
#     if visited[x][y] == 0:
#         if x < n - 1:
#             x += 1
#         else:
#             if y < n - 1:
#                 y += 1
#             else:
#                 y -= 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(graph, a, b):
        n = len(graph)
        queue = deque()
        queue.append(a, b)
        graph[]
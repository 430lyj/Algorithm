from sys import stdin
input = stdin.readline
R, C = tuple(map(int, input().split()))
arr = []

for _ in range(R):
    arr.append(list(input().rstrip()))

dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

A =  ord('A')
alphabet = [0] * 26
alphabet[ord(arr[0][0]) - A] = 1

def bfs (R, C, board):
    max_cnt = 0
    
    que = set()
    que.add((0, 0, arr[0][0]))
    while que :
        x, y, route = que.pop()
        max_cnt = max(max_cnt, len(route))
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < R and 0 <= temp_y < C:
                if board[temp_x][temp_y] not in route:
                    que.add((temp_x, temp_y, route + board[temp_x][temp_y]))
    return max_cnt

print(bfs(R, C, arr))
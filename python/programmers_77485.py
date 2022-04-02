def solution(rows, columns, queries):
    table = []
    for i in range(rows):
        table.append([j+i*columns for j in range(1, rows+1)])
    
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        cnt = ((x2 - x1) + (y2 - y1)) * 2
        k = table[x1][y1]
        cur_x, cur_y = x1, y1

        minimum = k
        while cnt > 0:
            cnt -= 1
            if cur_x == x1 and y1 <= cur_y < y2: # 위쪽 순회 중
                cur_y += 1
            elif x1 <= cur_x < x2 and cur_y == y2: # 오른쪽 순회 중
                cur_x += 1
            elif cur_x == x2 and y1 < cur_y <= y2: # 아래쪽 순회 중
                cur_y -= 1
            else:   # 왼쪽 순회 중
                cur_x -= 1
            temp = table[cur_x][cur_y]
            table[cur_x][cur_y] = k
            k = temp

            minimum = min(minimum, k)
        answer.append(minimum)
    return answer


r = 4
c = 3
queries = [[1,1,4,3]]
print(solution(r, c, queries))
def check_around(room, x, y):
    # 위, 아래, 왼, 오른, 오른쪽 아래 대각선, 왼쪽 위, 오른쪽 위, 왼쪽 아래 
    l = [1, 0, 1, 1] 
    r = [0, 1, 1, -1]
    
    for i in range(2): # 상하좌우 파악
        dx, dy = l[i], r[i]
        is_partition = False
        if 0 <= x+dx <= 4 and 0 <= y+dy <= 4:
            if room[x+dx][y+dy] == 'P':
                return False
            elif room[x+dx][y+dy] == 'X':
                is_partition = True
        dx, dy = 2*dx, 2*dy
        if 0 <= x+dx <= 4 and 0 <= y+dy <= 4 and room[x+dx][y+dy] == 'P':
            if not is_partition:
                return False
    
    for i in range(2, 4): # 대각선 확인
        dx, dy = l[i], r[i]
        if 0 <= x+dx <= 4 and 0 <= y+dy <= 4 and room[x+dx][y+dy] == 'P':
            # 파티션 존재하지 않는 경우
            if not (room[x+dx][y] == 'X' and room[x][y+dy] == 'X'): 
                return False
    return True
            
def check_place(place):
    x, y = 0, 0
    x_turn, y_turn = True, False
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                is_distanced = check_around(place, x, y)
                if is_distanced == False:
                    return 0
    return 1
            
def solution(places):
    answer = []
    is_distanced = True
    for idx_x, place in enumerate(places):
        is_distanced = check_place(place)
        answer.append(is_distanced)
    return answer

places = [["OPOXP", "OXOPO", "OPOOO", "OOOOO", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]]
print(solution(places))
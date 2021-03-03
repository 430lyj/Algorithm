def solution(k, room_number):
    roomLeft = []
    answer = []
    for i in range(k):
        roomLeft.append(i + 1)
    for i in range(len(room_number)):
        if room_number[i] in roomLeft:
            roomLeft.remove(room_number[i])
            answer.append(room_number[i])
        else:
            for j in range(len(roomLeft)):
                if room_number[i] < roomLeft[j]:
                    answer.append(roomLeft[j])
                    roomLeft.remove(roomLeft[j])
                    break

    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))
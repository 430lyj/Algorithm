import heapq

def solution1(operations):
    answer = []
    for operation in operations:
        if operation[0] == 'I':
            temp = operation.split()
            answer.append(int(temp[1]))
        elif len(answer) > 0:
            if operation[2] == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    if len(answer) == 0:
        answer = [0,0]
    else:
        max_value = max(answer)
        min_value = min(answer)
        answer = [max_value, min_value]
    return answer

def solution(operations):
    max_heap = []
    min_heap = []
    counter = 0
    for operation in operations:
        if operation[0] == 'I':
            temp = operation.split() 
            num = int(temp[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap,-1*num)
            counter += 1
        elif counter != 0:
            if operation[2] == '1':
                a = heapq.heappop(max_heap)
                min_heap.remove(-1*a)
            else:
                a = heapq.heappop(min_heap)
                max_heap.remove(-1*a)
            counter -= 1
    if counter == 0:
        return [0, 0]
    else:
        return[-1 * max_heap[0], min_heap[0]]
    return answer
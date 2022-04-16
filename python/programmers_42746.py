def solution(numbers):
    answer = ''
    for idx, number in enumerate(numbers):
        numbers[idx] = [str(number) * 3, len(str(number))]
    numbers.sort(reverse = True)
    for number in numbers:
        num, length = number[0], number[1]
        answer += num[:length]
    return str(int(answer))

def solution2(numbers):
    answer = ''
    for idx, number in enumerate(numbers):
        if number == 0:
            zero_cnt += 1
            continue
        arr = list(map(int, str(number)))
        real = len(arr)
        while len(arr) < 4:
            arr.append(arr[0])
        numbers[idx] = arr + [real]
    numbers.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3], x[4]))

    for number in numbers:
        i = 0
        while i < number[-1]:
            answer += str(number[i])
            i += 1
    return answer

numbers = [0, 1, 30]
print(solution(numbers))
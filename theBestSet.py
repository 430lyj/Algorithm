def solution(n, s):
    answer = []
    quotient = s // n
    remainder = s % n
    if quotient < 1:
        answer.append(-1)
    elif remainder == 0:
        for i in range(n):
            answer.append(quotient)
    else:
        for j in range(n - remainder):
            answer.append(quotient)
        for i in range(remainder):
            answer.append(quotient + 1)

    return answer

print(solution(5, 32))
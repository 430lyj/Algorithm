import math
def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1
    start = 1

    for station in stations:
        answer += max(math.ceil((station - w  - start) / W), 0)
        start = station + w + 1

    if start <= n:
        answer += math.ceil((n - start + 1) / W)

    return answer
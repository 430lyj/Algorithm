n = int(input())
num = []
# n_num = 0  # n_num은 n이 몇 번째 숫자인지 알려줌
# for_3 = n // 3
# for_5 = n // 5
# for_15 = n // 15
# n_num = n - for_3 - for_5 + for_15 
arr = []
left, right = n, 3*n
while left <= right:
    mid = (left + right) // 2  
    if mid % 3 == 0 or mid % 5 == 0: # 만약 mid가 숫자가아닌 moo 라면
        mid += 1
    num3 = mid // 3
    num5 = mid // 5
    num15 = mid // 15
    value = mid - num3 - num5 + num15 # mid가 몇 번째 수인지 확인
    if value > n:      # 만약 n번째 수가 mid보다 작다면
        right = mid -1 # mid의 왼쪽 탐색
    elif value < n:    # 만약 n번째 수가 mid보다 크다면 
        left = mid + 1  # mid의 오른쪽 탐색
    elif value == n:    # 만약 n번째 수 == mid 이라면
        print(mid)      # mid 값 프린트
        break
n, m = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 1, arr[-1] - arr[0] # 가장 인접한 두 물건의 거리 최소값, 가능한 최대값
result = 0

while left <= right:    
    mid = (left + right) // 2
    cnt = 1
    current = arr[0]
    possible = False

    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            if arr[i] == current + mid:
                possible = True
            cnt += 1
            current = arr[i]
            
    
    if cnt >= m:
        left = mid+1
        if possible :
            result = mid 
    else:
        right = mid - 1

print(result)
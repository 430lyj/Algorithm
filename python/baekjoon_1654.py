K, N = tuple(map(int, input().split()))

arr = []

for _ in range(K):
    arr.append(int(input()))
    
max_val = max(arr)
count = 0
while count < N:
    count = 0
    mid = max // 2
    for elem in arr:
        count += elem // mid

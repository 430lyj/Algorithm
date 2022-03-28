n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    l = arr[0]
    arr.pop(0)
    average = sum(arr) / len(arr)
    count = 0
    for elem in arr:
        if elem > average:
            count += 1
    ans = (count / l) * 100
    print('%.3f' % ans, end='')
    print('%')

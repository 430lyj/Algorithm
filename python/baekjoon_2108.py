from audioop import avg


N = int(input())
from collections import Counter

arr = []
for _ in range(N):
    arr.append(int(input()))

sorted_arr = arr.sort()
print(sum(arr)// N)
mid = N // 2
dic = {}
max_count, max_val = 0, 0
for elem in arr:
    if elem in dic.keys():
        dic[elem] += 1
    else:
        dic[elem] = 1
    if dic[elem] > max_count:
        max_count = dic[elem]
        max_val = elem


print(max_val)
print(sorted_arr[mid-1])
print(sorted_arr[-1] - sorted_arr[0])

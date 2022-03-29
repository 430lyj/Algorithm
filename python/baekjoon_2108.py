import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input())) 

print(round(sum(arr)/N))

arr.sort()
mid = N // 2
print(arr[mid])

nums = Counter(arr).most_common()
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])
    
print(arr[-1] - arr[0])
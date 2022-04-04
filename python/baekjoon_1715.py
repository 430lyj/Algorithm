import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

sums = 0
total_compare = sums

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sums = a + b
    total_compare += sums
    heapq.heappush(arr, sums)

if n == 1:
    print(0)
else:
    print(total_compare)
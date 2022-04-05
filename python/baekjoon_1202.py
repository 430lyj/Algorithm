import heapq, sys
input = sys.stdin.readline
N, K = tuple(map(int, input().split()))
jewels = []
bags = []

jewels = []
for _ in range(N):
    m, v = tuple(map(int, input().split()))
    heapq.heappush(jewels, (m, v))


for _ in range(K):
    c = int(input())
    bags.append(c)
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jewels and bag >= jewels[0][0]: # 보석이 남았고, 가방 안에 가장 첫 번째 보석 들어갈 수 있음.
        heapq.heappush(tmp_jew, -heapq.heappop(jewels)[1]) # 보석 가치 추가
    if tmp_jew :
        answer -= heapq.heappop(tmp_jew)
    elif not jewels:
        break
print(answer)
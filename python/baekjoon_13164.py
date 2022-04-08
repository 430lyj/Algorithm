N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
minus = []

for i in range(1, N):
    minus.append(arr[i]-arr[i-1])

minus.sort()
answer = 0
for i in range(N - K):
    answer += minus[i]

print(answer)
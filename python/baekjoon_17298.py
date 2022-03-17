import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
stack = []
for i in range(n):
    while stack and  arr[stack[-1]] < arr[i] :
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)

# left, right = 0, 0
# while left <= right and right < n:
#     if query[left] >= query[right]: # 기준점이 오른쪽 포인터보다 크거나 같음.
#         right += 1
#     else:
#         answer.append(query[right])
#         left += 1
#     if right == n and left != right:
#         answer.append(-1)
#         left += 1
#         right = left




N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
sort_arr = sorted(arrA)
answer = 0 
no_cnt = 0
for i in range(N-1, -1, -1):
    if arrB[i] == sort_arr[i]:
        no_cnt += 1
    else:
        break

for i in range(no_cnt):
    arrA.remove(sort_arr[N-1-i])
arrB = arrB[:N-no_cnt]
print(arrA)
print(arrB)

if no_cnt == N:
    answer = 1

for i in range(len(arrA)-1, 0, -1):
    for j in range(i):
        if arrA == arrB:
            answer = 1
            break
        if arrA[j] > arrA[j+1]:
            arrA[j], arrA[j+1] = arrA[j+1], arrA[j]
    if answer == 1:
        break

print(answer)
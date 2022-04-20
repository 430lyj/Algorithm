N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(K):
    if arr[i] in plug:
        continue
    if len(plug) < N:
        plug.append(arr[i])
        continue

    idxs = []
    for j in range(N):
        try:
            idx = arr[i:].index(plug[j])
        except:
            idx = 101
        idxs.append(idx)

    plug_out = idxs.index(max(idxs))
    del plug[plug_out]
    plug.append(arr[i])
    cnt += 1
print(cnt)
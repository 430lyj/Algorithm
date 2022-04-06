import sys
MAX_INT = sys.maxsize

n = int(input())
m = int(input())
buses = [[] for _ in range(n)]
arr = [tuple(map(int, input().split())) for _ in range(m)]
start, end = tuple(map(int, input().split()))

for city1, city2, price in arr:
    buses[city1-1].append((city2-1, price))

start -= 1  # 인덱스화
end -= 1    # 인덱스화
minimum_price = [[MAX_INT, []] for _ in range(n)] 
minimum_price[start] = [0, [start]]
visited = [0] * n
visited[start] = 1
last_visited = start
while last_visited != end:
    minimum_dist = MAX_INT
    candidate = last_visited
    for city, price in buses[last_visited]:
        if visited[city] == 0 and minimum_price[city][0] > price + minimum_price[last_visited][0]:
            minimum_price[city][0] = price + minimum_price[last_visited][0]
            minimum_price[city][1] = minimum_price[last_visited][1] + [city]
            if minimum_price[city][0] < minimum_dist:
                minimum_dist = minimum_price[city][0]
                candidate = city
                                                                                                                  
    last_visited = candidate 
    visited[last_visited] = 1
print(minimum_price[end][0])
print(len(minimum_price[end][1]))
for i in minimum_price[end][1]:
    print(i+1, end=" ")
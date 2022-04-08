def solution(m, n, puddles):
    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                graph[j][i] = 1
            elif [i, j] not in puddles:
                graph[j][i] = (graph[j-1][i] + graph[j][i-1]) % 1000000007
    return graph[n][m]
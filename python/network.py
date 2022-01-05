visited = list()
stack = list()
parent = list()

#dfs algorithm - using stack
def solution (n, computers):
    answer = 0
    for i in range(n):
        if i not in visited:
            stack.append(i) #탐색 시작 노드를 스택에 삽입한다.
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.append(v)
                    for j in range(n):
                        #j는 v의 인접 노드 중 아직 방문하지 않은 모든 노드이다. j를 찾아서 stack에 추가한다.
                        if computers[v][j] == 1 and j not in visited:
                            stack.append(j)
            answer += 1 #한 네트워크의 노드 전체를 찾을 때마다 네트워크 +1 해준다.
    return answer
  #출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

def solution(n, k, cmd):
    answer = ['O'] * n
    nodes = {i : [i-1, i+1] for i in range(n)}
    nodes[0] = [None, 1]
    nodes[n-1] = [n-2, None]
    stack = []
    
    for c in cmd:
        if c.startswith("C"):
            answer[k] = 'X'
            before, after = nodes[k]
            if before != None:
                nodes[before][1] = nodes[k][1]
            if after != None:
                nodes[after][0] = nodes[k][0]

            stack.append([before,k, after])
            k = nodes[k][0] if nodes[k][1] == None else nodes[k][1]
                
        elif c.startswith("Z"):
            before, z, after = stack.pop()
            answer[z] = 'O'
            if after != None:
                nodes[after][0] = z
            if before != None:
                nodes[before][1] = z

        else:   
            command, idx = c.split()
            idx = int(idx)
            if command == 'D':
                while idx != 0 and nodes[k][1] != None:
                    idx -= 1
                    k = nodes[k][1]

            else:
                while idx != 0 and nodes[k][0] != None:
                    idx -= 1
                    k = nodes[k][0]

        
    final = ''        
    for elem in answer:
        final += elem
    return final

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))
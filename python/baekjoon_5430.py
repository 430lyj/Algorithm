def solution(n, cmds, arr):
    rev = False
    for cmd in cmds:
        if cmd == 'R':
            if rev == False:
                rev = True
            else:
                rev = False
        elif cmd == 'D':
            if len(arr) > 0:
                if rev == False:
                    del arr[0]
                else:
                    del arr[-1]
            else:
                print('error')
                return
    if rev == True:
        arr.reverse()
        print('[' + ','.join(arr) + ']')
    else:
        print('[' + ','.join(arr) + ']')


T = int(input())

for _ in range(T):
    cmds = list(input())
    n = int(input())
    input_arr = input().lstrip('[').rstrip(']')
    arr = [] if input_arr == '' else list(input_arr.split(','))
    solution(n, cmds, arr)
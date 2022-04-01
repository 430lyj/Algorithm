import sys
input = sys.stdin.readline
n = int(input())

def special_fact(a, b, c, fact_dp): # a! / (b! * c!) 값을 리턴해주는 함수
    return fact_dp[a] / (fact_dp[b] * fact_dp[c])
    
    
def solution(n):
    answer = 1
    fact_dp = [1] * (n+1)
    for i in range(1, n+1):
        fact_dp[i] = i * fact_dp[i-1]

    possible_comb = (n // 2)+ 1
    for i in range(1, possible_comb):
        cnt1 = n - i*2  #1의 개수
        answer += special_fact(n-i, cnt1, i, fact_dp)
    return answer % 1000000007

print(solution(n))
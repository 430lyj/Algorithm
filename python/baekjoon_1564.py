n = int(input())

num = 1
for i in range(2, n+1):
    num *= i
    while num % 10 == 0:
        num //= 10
    num %= 100000000000000000

print(str(num).rstrip('0')[-5:])
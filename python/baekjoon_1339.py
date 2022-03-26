n = int(input())
number = 9
arr = []
dic = {}
converted_letters = {}
for _ in range(n):
    x = input()
    x = x[::-1]
    for idx, letter in enumerate(x):
        if letter in converted_letters.keys():
            converted_letters[letter] += 10 ** idx
        else:
            converted_letters[letter] = 10 ** idx

converted_letters = {k: v for k, v in sorted(converted_letters.items(), key=lambda item: item[1])}
answer = 0
for val in reversed(converted_letters.values()):
    answer += val * number
    number -= 1
print(answer)
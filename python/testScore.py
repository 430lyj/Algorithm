def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 2, 1, 2, 2, 4, 4, 5, 5]
    correct1 = 0
    correct2 = 0
    correct3 = 0
    n = len(answers)
    for i in range(n):
        if answers[i] == person1[i % 5]:
            correct1 += 1
        if answers[i] == person2[i % 8]:
            correct2 += 1
        if answers[i] == person3[i % 10]:
            correct3 += 1
    correct = [correct1, correct2, correct3]
    MAX = max(correct)
    for i in range(3):
        if correct[i] == MAX:
            answer.append[i]
    return answer
  # 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

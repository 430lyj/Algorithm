def solution(nums):
    myPonketmon = len(nums) / 2
    numberofSpices = len(set(nums))
    answer = 0
    
    if numberofSpices > 200000 or numberofSpices < 1:
        answer = 0
    elif numberofSpices > myPonketmon:
        answer = myPonketmon
    else:
        answer = numberofSpices
        
    return answer

print(solution([1, 3, 3, 2, 5, 6]))
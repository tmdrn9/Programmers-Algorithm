def solution(sides):
    temp=max(sides)
    #sides의 최대값이 가장 긴 변일 때
    answer=set(range(abs(sides[0]-sides[1])+1,temp+1))
    #나머지 한 변이 가장 긴 변일 때
    answerr=answer.union(set(range(temp+1,sum(sides))))
    return len(answerr)

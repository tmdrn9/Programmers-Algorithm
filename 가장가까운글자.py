def solution(s):
    d=dict()
    answer = []
    for i,n in enumerate(s):
        if s.count(n,0,i+1)==1:
            answer.append(-1)
        else:
            answer.append(i-d[n])
        d[n]=i
    return answer

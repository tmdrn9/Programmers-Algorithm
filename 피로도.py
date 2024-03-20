from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons=permutations(dungeons,len(dungeons))
    for i in dungeons:
        temp=0
        kk=k
        for j in i:
            if kk>=j[0]:
                kk-=j[1]
                temp+=1
            else:
                continue
        if temp>=answer:
            answer=temp
    return answer

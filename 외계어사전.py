def solution(spell, dic):
    answer=2
    for i in dic:
        if len(i)!=len(spell):
            continue
        for j in i:
            if j not in spell:
                answer=2
                break
            elif i.count(j)!=1:
                answer=2
                break
            else:
                answer=1
                continue
        if answer==1:
            return answer
    return answer

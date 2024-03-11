'''
itertools.permutations(리스트, 요소 개수)
소수찾기는 range(2, int(math.sqrt(n)) + 1) 기억하기
좀더 짧게 할 수 있었을듯
'''

import itertools, math
def solution(numbers):
    number_li=[i for i in numbers]
    answer = 0
    combi=[]
    for k in range(len(number_li)):
        combi.extend(list(itertools.permutations(number_li,k+1)))   
    n_li=[]
    for j in combi:
        temp=''
        for k in range(len(j)):
            temp+=j[k]
        n_li.extend([int(temp)])
    n_li=list(set(n_li))
    
    if 0 in n_li:
        del n_li[n_li.index(0)]
    if 1 in n_li:
        del n_li[n_li.index(1)]

    for n in n_li:
        ch=0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i==0:
                ch=1
                break
        if ch==0:
            answer+=1
    return answer

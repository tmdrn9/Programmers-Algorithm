#python에서 queue는 그냥 list

def solution(s):
    ss=s.split()
    answer = 0
    if 'Z' in ss:
        while len(ss)>0:
            c=ss.pop()
            if c=='Z':
                ss.pop()
            else:
                answer+=int(c)
        return answer
    else:
        ss=list(map(int,ss))
        return sum(ss)

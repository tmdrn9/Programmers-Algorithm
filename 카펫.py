def solution(brown, yellow):
    answer = []
    temp=int((brown/2)+2)
    for i in range(1,int(temp/2)+1):
        x,y=temp-i,i
        if ((x*y)-brown)==yellow:
            return [x,y]

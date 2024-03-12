'''
" ".join(str_list):list요소들 다 합치기
str로 처리해서 하는건 바로 파악했으나 itertools를 사용해 모든 조합을 구해서 시간초과
힌트보고 품
'''
import itertools
def solution(numbers):
    str_li=list(map(str,numbers))
    str_li.sort(key=lambda x: (x * 4)[:4], reverse=True) 
    #numbers의 원소의 최대 자리수가 4개이기때문에 *4하고 4자리수까지 끊기
    answer=str(int("".join(str_li)))
    return answer

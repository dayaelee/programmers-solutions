def solution(n, s):
    answer = []
    
    tmp = s//n
    tmp2 = s%n
    s = [tmp] * n
    
    tmp = list(set(s))
    
    if len(tmp)==1 and tmp[0]==0:
        return [-1]
    
    for i in range(tmp2):
        s[i]+=1
    
    s.sort()
    
    return s
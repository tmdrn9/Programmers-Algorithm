def solution(wallpaper):
    lox=[]
    loy=[]
    
    for i,r in enumerate(wallpaper):
        for ii,cc in enumerate(r):
            if cc=='#':              
                lox.append(i)
                loy.append(ii)
    luy=min(loy)
    rdy=max(loy)
    return [lox[0],luy,lox[-1]+1,rdy+1]

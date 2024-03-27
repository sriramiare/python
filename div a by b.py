def div_ab(n,d):
    if d==0 or n<0 or d<0:
        return None
    q=n//d
    r=n%d
    if r==0:
        return q
    res=[]
    res.append(str(q))
    res.append(".")
    rem_map={}
    while r!=0:
        if r in rem_map:
            res.insert(rem_map[r],'')
            res.append('...')
            return "".join(res)
        else:
            rem_map[r]=len(res)
            r=r*10
            q=r//d
            res.append(str(q))
            r=r%d
    return "".join(res)
n=int(input("enter numerator:"))
d=int(input("enter denominator:"))
print("ans:",div_ab(n,d))

n,m=map(int,input().split())
x=0
while m>0:
    x+=1
    m-=x
    if x==n:
        x=0
    if m<=x:
        m=m
        break
    
print(m)

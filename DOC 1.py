d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
a=list(d1.values())
b=list(d2.values())
a1=list(d1.keys())
b1=list(d2.keys())
i=0
d={}
while i<len(a1):
    if a1[i]==b1[i]:
        sum=a[i]+b[i]
        d[b1[i]]=sum
    else:
        d[b1[i]]=b[i]
        d[a1[i]]=a[i]
    i+=1
print(d)

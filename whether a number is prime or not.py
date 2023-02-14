# a=int(input("enter the number"))
# if (a<=1):
#     print("not a prime number")
# else:
#     b=1
#     for i in range(2,a//2):
#         if (a%i==0):
#             print("not a prime number")
#             b=0
#             break
#     if (b==1):
#         print(")



j=int(input())
for i in range(j):
    x,y,z=map(int,input().split())
    a=x+y  
    b=y+z 
    c=z+x 
    if a==z:
        print("yes")
    elif b==x:
        print("yes")
    elif c==y:
        print("yes")
    else:
        print("no")
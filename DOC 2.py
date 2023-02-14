str=str(input("enter the string"))
dic={}
for a in str:
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
dict={}
for key in dic:
    dict[key]=dic[key]
    # print(key,':',dic[key])
print(dict)

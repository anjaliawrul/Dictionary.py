# a={1:"one",2:"two"}
# b={3:"three",4:"four"}
# a.update(b)
# print(a)


# or
a={1:"one",2:"two"}
b={3:"three",4:"four"}
c={**a,**b}
print(c)
# zad1 i zad 2
x=0
y=1
land=[]
def bramkaAnd(a,b):
    if a==b and a==1:

        return True
    else :
        return False
land.append(bramkaAnd(y,y))
land.append(bramkaAnd(x,y))
land.append(bramkaAnd(x,x))
land.append(bramkaAnd(y,x))
lor=[]
def bramkaOR(a,b):
    if a==1 and a!=b or b==1 and b != a:

        return True
    else :
        return False
lor.append(bramkaOR(y,y))
lor.append(bramkaOR(x,y))
lor.append(bramkaOR(x,x))
lor.append(bramkaOR(y,x))
def bramkaNOT(a):
    if a==1:

        return False
    else :
        return True
lnot=[]
lnot.append(bramkaNOT(y))
lnot.append(bramkaNOT(y))
lnot.append(bramkaNOT(x))
lnot.append(bramkaNOT(x))
print("     yy    xy    xx    yx  ")
print("and",land)
print("or",lor)
print("not",lnot)
zad 3
x=0
y=1
def complex(a,b,c):
    if a==1 and a==b :
        return True
    else :
        return not c

print("000",complex(x,x,x))
print("010",complex(x,y,x))
print("100",complex(y,x,x))
print("001",complex(x,x,y))
print("011",complex(x,y,y))
print("101",complex(y,x,y))
print("110",complex(y,y,x))
print("111",complex(y,y,y))

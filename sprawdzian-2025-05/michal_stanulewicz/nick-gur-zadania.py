import math

#fibonaczi
n=int(input("podaj liczbe operacji"))
def Ciag(n):
        l=[0]
        x, y = 0, 1
        for i in range(n-1):
            y += x
            x = y - x
            l.append(x)
        return(l)

print("liczba operacji",Ciag(n))
#NWW
def nww(a,b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b)//nwdrekurencyjne(a,b)

#nwd
a=int(input("podaj 1 liczbe"))
b=int(input("podaj2 liczbe"))
def nwditeracjyjne(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
        return a
print(nwditeracjyjne(a,b))
def nwdrekurencyjne(a,b):
    if b>0:
        return nwdrekurencyjne(b,a%b)
    return a
print(nwdrekurencyjne(a,b))
#ulamki

def skroculamek(a,b):
    x= True
    while x ==True:
     u=nwdrekurencyjne(a,b)
     a=a/u
     b=b/u
     if a/nwdrekurencyjne(a,b)==1:
         break
     return(a/b)
print(skroculamek(a,b))
def dodaj(licz1,mianownik1,licz2,mianownik2):
    u2=nww(mianownik2,mianownik2)
    licz1=licz1*(u2/mianownik1)
    licz2=licz2*(u2/mianownik2)
    print(licz1 +licz2,"/",u2)
    dodaj(1, 2,1,3 )
def odejmij(licz1,mianownik1,licz2,mianownik2):
    u2=nww(mianownik2,mianownik2)
    licz1=licz1*(u2/mianownik1)
    licz2=licz2*(u2/mianownik2)
    print(licz1 -licz2,"/",u2)
    odejmij(3, 4,1,2)
#erastotenes
he=int(input("podaj liczbe"))

def erastotenes(he):
    nic=[True for i in range(n+1)]
    nic[0]=nic[1]=False
    pierwsze=[]
    for i in range(2,int(n*0.5)+1):
        if nic[i]:
            for j in range(i*i,n,i):
                nic[j]=False
    pierwsze=[x for x in range(n) if nic[x]==True]
    return pierwsze

print(erastotenes(he))

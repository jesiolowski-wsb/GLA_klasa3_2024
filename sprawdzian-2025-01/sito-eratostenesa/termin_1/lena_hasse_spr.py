import time
start_time = time.time()
czas = time.time() - start_time

def czy_pierwsza_pelne(x):
    if x<2:
        return False
    for i in range(2,x+1):
        if x%i==0:
            return False
    return True


def sito_pelne(n):
    for i in range(0,n+1):
        if czy_pierwsza_pelne(i):
            print(i,end=', ')


def czy_pierwsza_optymalne(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True


def sito_optymalne(n):
    for i in range(0,n+1):
        if czy_pierwsza_optymalne(i):
            print(i,end=', ')


sito_optymalne(20)

#zad 4 z powodu, ze powyzej pierwiastka z n mamy wielokrotnosci z przedzialu 2-n to finalnie wychodzi to samo
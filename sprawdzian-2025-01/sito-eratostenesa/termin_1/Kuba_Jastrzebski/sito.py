from math import sqrt, ceil
from time import time

#zad.1
def sito_eratostenesa(n):
    odp = []
    liczby = [True for i in range(n+1)]
    liczby[0] = False
    liczby[1] = False
    counter = 0
    for i in range(2, n + 1):
        if liczby[i]:
            for j in range(i ** 2, n + 1, i):
                liczby[j] = False
    for index, i in enumerate(liczby):
        if i: odp.append(index)
    return odp

#zad.2

def sito_pelne(n):
    odp = []
    liczby = [True for i in range(n+1)]
    liczby[0] = False
    liczby[1] = False
    counter = 0
    operation_counter = 0
    for i in range(2, n + 1):
        counter += 1
        if liczby[i]:
            operation_counter += 1
            for j in range(i ** 2, n + 1, i):
                liczby[j] = False
                operation_counter += 1
    for index, i in enumerate(liczby):
        if i: odp.append(index)
    return odp, counter, operation_counter

def sito_optymalne(n):
    odp = []
    liczby = [True for i in range(n+1)]
    liczby[0] = False
    liczby[1] = False
    counter = 0
    operation_counter = 0
    for i in range(2, ceil(sqrt(n))):
        counter += 1
        if liczby[i]:
            operation_counter += 1
            for j in range(i ** 2, n + 1, i):
                liczby[j] = False
                operation_counter += 1
    for index, i in enumerate(liczby):
        if i: odp.append(index)
    return odp, counter, operation_counter


start = time()
print(sito_optymalne(10000)[0])
print("Liczba iteracji:", sito_optymalne(10000)[1])
print("Liczba operacji:", sito_optymalne(10000)[2])
czas = time() - start
print(czas)
start = time()
print(sito_pelne(10000))
print("Liczba iteracji:", sito_pelne(10000)[1])
print("Liczba operacji:", sito_pelne(10000)[2])
czas = time() - start
print(czas)
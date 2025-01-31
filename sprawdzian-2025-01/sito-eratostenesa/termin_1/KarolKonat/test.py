from math import sqrt
from time import time



def porownaj_wydajnosc(n):
    print(f"Porównanie wydajności dla n = {n}")
    print("-" * 50)
    
    wyniki_pelne = sito_pelne(n)
    wyniki_optymalne = sito_optymalne(n)
    
    print(f"{'Wersja':<15} {'Iteracje':<12} {'Operacje':<12} {'Czas':<8}")
    print("-" * 50)
    print(f"{'Pełna':<15} {wyniki_pelne[1]:<12} {wyniki_pelne[2]:<12} {wyniki_pelne[3]:.4f}s")
    print(f"{'Optymalna':<15} {wyniki_optymalne[1]:<12} {wyniki_optymalne[2]:<12} {wyniki_optymalne[3]:.4f}s")
    
    roznica_iteracji = ((wyniki_pelne[1] - wyniki_optymalne[1]) / wyniki_pelne[1]) * 100
    print(f"\nOptymalizacja zmniejszyła liczbę iteracji o {roznica_iteracji:.2f}%")



def sito_eratostenesa(n, stop_value=None, meassure=False):
	s = time()
	if not stop_value: stop_value = sqrt(n)+1
	prime_tbl = [True for _ in range(n)]
	prime_tbl[0] = False
	prime_tbl[1] = False

	main_iter = 0
	oper = 0

	for i in range(2, int(stop_value)):
		main_iter += 1
		if not prime_tbl[i]: 
			continue

		oper += 1
		for j in range(i*i, n, i):
			oper += 1
			prime_tbl[j] = False

	if not meassure:
		return [a for a in range(len(prime_tbl)) if prime_tbl[a]]
	return [a for a in range(len(prime_tbl)) if prime_tbl[a]], main_iter, oper, time()-s

def sito_pelne(n):
	return tuple(sito_eratostenesa(n, stop_value=n, meassure=True))

def sito_optymalne(n):
	return tuple(sito_eratostenesa(n, meassure=True))

porownaj_wydajnosc(1000000)


"""
ODPOWIEDŹ NA PYTANIE 4

Algorytm sprawdza kolejne wielokrotności liczb x z przedziału (0, k) do n, więc dla rozwiązania optymlnego k = sqrt(n), ponieważ jest to największe x dla którego istnieją
jeszcze wielokrotności nie sprawdzone przez poprzednie a, które są < n. 
"""

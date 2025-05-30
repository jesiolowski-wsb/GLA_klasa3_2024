# zdobyte punkty 6/6
# ✅ Algorytm działa poprawnie i zwraca prawidłowe wyniki
# 💡 Dobra optymalizacja z sqrt(n) i elegancka list comprehension na końcu

from math import sqrt

def znajdz_pierwsze(n):
	primes = [True for i in range(n+1)]
	primes[0] = False
	primes[1] = False

	for i in range(2, int(sqrt(n))+1):
		if not primes[i]: continue
		for j in range(i, n):
			if i*j > n: break
			primes[i*j] = False

	return [i for i in range(n+1) if primes[i]]

print(znajdz_pierwsze(20))



# zdobyte punkty: 4/6
# ✅ Podstawowa logika algorytmu jest zrozumiała i kod działa
# ❌ Krytyczny błąd: for j in range(i, len(numbers), i): wykreśla także samą liczbę pierwszą i (powinno być range(i*i, len(numbers), i))
# ❌ Tablica numbers = [True for _ in range(n)] ma rozmiar n zamiast n+1, więc dla sito(20) nie sprawdza liczby 20

def sito(n):
    numbers = [True for _ in range(n)]
    primes = []

    for i in range(len(numbers)):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i] == True:
                primes.append(i)

                for j in range(i, len(numbers), i):
                    numbers[j] = False

    return primes

print(sito(30))

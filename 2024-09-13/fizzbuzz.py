# Wypisz liczby od 1 do 100, z czego:
# gdy liczba podzielna na 3 wypisz Fizz
# gdy liczba podzielna na 5 wypisz Buzz
# gdy liczba podzielna przez zarówno 3 i 5 wypisz FizzBuzz

# przed zrobieniem zadania:
# funkcje: def X(): (return vs print() )
# range(od, do, [step])

# debugger

def fizzbuzz(n):
    for liczba in range(1, n + 1):
        if liczba % 3 == 0 and liczba % 5 == 0: # alternatywnie => liczba % 15 == 0
            print("FizzBuzz")
        elif liczba % 3 == 0:
            print("Fizz")
        elif liczba % 5 == 0:
            print("Buzz")
        else:
            print(liczba)

# Wywołaj funkcję fizzbuzz z określoną liczbą n (np. 100)
n = 100
fizzbuzz(n)

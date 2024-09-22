# napisać funkcję obliczającą n-ty element ciągu fibonacciego z użyciem rekurencji
# teoria ciągu fibonacciego: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego

# Use case: populacja królików
# Problem: Załóżmy, że masz jedną parę królików. Króliki osiągają dojrzałość po jednym miesiącu,
# a od drugiego miesiąca zaczynają rodzić kolejną parę królików co miesiąc. Przyjmijmy, że:
# - Każda nowa para zaczyna rozmnażać się po ukończeniu jednego miesiąca życia.
# - Żadna para królików nie umiera.

# Ile par królików będziesz miał po n miesiącach?

# Liczba par królików w danym miesiącu jest wyrazem ciągu Fibonacciego,
# ponieważ liczba królików w danym miesiącu to suma liczby królików w dwóch poprzednich miesiącach:
#
# W miesiącu 0: 1 para
# W miesiącu 1: 1 para (bo pierwsza para się jeszcze nie rozmnaża)
# W miesiącu 2: 2 pary (pierwsza para się rozmnożyła)
# W miesiącu 3: 3 pary (druga para się rozmnaża)
# I tak dalej...

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(f"fib(0): {fib(0)}")
print(f"fib(1): {fib(1)}")
print(f"fib(2): {fib(2)} (1+0)")
print(f"fib(3): {fib(3)} (1+1)")
print(f"fib(4): {fib(4)} (2+1)")
print(f"fib(5): {fib(5)} (3+2)")
print(f"fib(6): {fib(6)} (5+3)")
print(f"fib(7): {fib(7)} (8+5)")
print(f"fib(8): {fib(8)} (13+8)")
print(f"fib(9): {fib(9)} (21+13)")
print(f"fib(10): {fib(10)} (34+21)")


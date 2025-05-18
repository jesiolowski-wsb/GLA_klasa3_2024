# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) dla n > 1

def fib_rekurencyjnie(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rekurencyjnie(n-1) + fib_rekurencyjnie(n-2)


def fib_iteracyjnie(n):
    if n <= 0:
        return 0

    a, b = 0, 1  # F(0), F(1)

    for i in range(2, n + 1):
        a, b = b, a + b

    return b if n > 0 else a


print(fib_iteracyjnie(6))
def fib_rekurencyjnie(n):
    obliczone = {0: 0, 1: 1}

    def fib_pamietajace(k):
        if k in obliczone:
            return juz_obliczone[k]

        obliczone[k] = fib_pamietajace(k - 1) + fib_pamietajace(k - 2)
        return obliczone[k]
    wyniki = []
    for i in range(n):
        wyniki.append(fib_pamietajace(i))

    return wyniki
def fib_iteracyjnie(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    wyniki = [0, 1]
    for i in range(2, n):
        wyniki.append(wyniki[i - 1] + wyniki[i - 2])

    return wyniki

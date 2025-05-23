#def fib_rekurencyjnie(n):
#    output = []
#    if n == 0: return 0
#    if n == 1: return 1
#    return fib_rekurencyjnie(n - 1) + fib_rekurencyjnie(n - 2)

def fib_iteracyjnie(n):
    output = [0, 1]
    for i in range(n-2):
        output.append(output[-1] + output[-2])
    return output

#print(fib_rekurencyjnie(10))
print(fib_iteracyjnie(10))
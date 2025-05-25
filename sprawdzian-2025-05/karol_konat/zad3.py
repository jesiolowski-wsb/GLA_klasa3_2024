def __fib_rec(n, tbl):
	tbl_len = len(tbl)
	if tbl_len == n:
		return

	tbl.append(tbl[tbl_len-1] + tbl[tbl_len-2])
	__fib_rec(n, tbl)

def fib_rekurencyjnie(n):
	fibs = []
	fibs.append(0)
	fibs.append(1)
	__fib_rec(n, fibs)
	return fibs

def fib_iteracyjnie(n):
	fibs = [0 for i in range(n)]
	fibs[0] = 0
	fibs[1] = 1
	for i in range(2, n):
		fibs[i] = fibs[i-1]+fibs[i-2]

	return fibs


print(fib_rekurencyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib_iteracyjnie(10))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
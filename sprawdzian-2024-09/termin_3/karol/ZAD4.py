def lucky_number(n):
	if n%2 == 0:
		print("Lucky", end='')
	if n%7 == 0:
		print("Number", end='')
	elif n%2 != 0:
		print(n, end='')

	print('')

while True:
	lucky_number(int(input("Podaj liczbę: ")))
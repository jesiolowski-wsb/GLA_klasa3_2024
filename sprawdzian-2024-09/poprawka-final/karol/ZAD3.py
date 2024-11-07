# Zdobyte punkty: 5/5
from random import randint

def gierka():
	n = randint(1, 100)

	print("Zgadnij liczbę od 1 do 100")
	a = input('>> ')

	if a.lower() == 'koniec':
		print("Dziękuje za gre!")
		return False

	a = int(a)

	while a != n:
		if a < n:
			print("Za mało!")
		else:
			print("Za dużo!")
		a = int(input('>> '))

	print("Brawo ty. Zgadles")

	return True


while True:
	# ładneeeeeee :D
	if not gierka():
		break
	c = input("Chcesz zagrać dalej (T/n): ")
	# tutaj ciut przekombinowane ze sluchamy zarówno na 'koniec' jak i 'n', tyle ze w innych miejscach
	# czyściej byłoby miec te funkcjonalnosc w jednym miejscu
	if c.lower() == 'n':
		print("Dziękuje za gre!")
		break
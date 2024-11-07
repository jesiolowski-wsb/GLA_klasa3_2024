# Zdobyte punkty: 9/7
def odwroc_liste(lista):
	if len(lista) < 2:
		return lista

	# boze, ale Ty kombinujesz :D Rozumiem ze to dlatego ze o to prosilem?
	l = odwroc_liste(lista[1:-1])
	l.append(lista[0])
	l.insert(0, lista[-1])
	return l

print(odwroc_liste([1, 2, 3, 4, 5]))
print(odwroc_liste(['a', 'b', 'c']))


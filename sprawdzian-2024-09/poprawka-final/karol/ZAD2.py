def odwroc_liste(lista):
	if len(lista) < 2:
		return lista


	l = odwroc_liste(lista[1:-1])
	l.append(lista[0])
	l.insert(0, lista[-1])
	return l

print(odwroc_liste([1, 2, 3, 4, 5]))
print(odwroc_liste(['a', 'b', 'c']))
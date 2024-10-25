plik= open('analiza.txt', 'r')
zawartosc= plik.read()
dane=zawartosc.split()
print(dane)
lista=[x for x in dane if len(x)>3 and x[0].isupper()]
print(lista)
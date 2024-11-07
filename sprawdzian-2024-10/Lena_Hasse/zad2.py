# Zdobyte punkty: 4/5

plik= open('analiza.txt', 'r')
zawartosc= plik.read()
dane=zawartosc.split()
print(dane)
lista=[x for x in dane if len(x)>3 and x[0].isupper()]

# kurdeeee, a gdzie zapis do pliku :((((
print(lista)


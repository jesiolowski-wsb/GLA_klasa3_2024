# Zdobyte punkty: 5/5

def osemkowy_binarny(liczba):
    wynik=int(liczba,8)
    return bin(int(wynik))[2:]

with open('oct.txt','r') as plik:
    tekst=plik.read()
lista=tekst.split()

with open('bin.txt','w') as wynik:
    for liczba in lista:
        # wiesz co, niepotrzebnie wywolujesz funkcje osemkowy_binarny w tej linii
        if len(osemkowy_binarny(liczba))>3:
            # a potem raz jeszcze w tej. W 'prawdziwym swiecie' te obliczenia mogą być cięęęęęęęęęęężkie,
            # a to znaczy ze lepiej byloby wykonac je raz, a potem odwolywac sie do wartosci przechowanej w zmiennej
            wynik.write(osemkowy_binarny(liczba)+'\n')
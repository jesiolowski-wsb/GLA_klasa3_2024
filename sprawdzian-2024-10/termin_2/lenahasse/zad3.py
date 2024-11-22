# Zdobyte punkty: 5/6

import random
def generuj_kod():
    litery='qwertyuioplkjhgfdsazxcvbnm'
    cyfry='1234567890'
    wynik=''

    # w wypadkach gdy tworzymy zmienną której wartości nie potrzebujemy użyć (jak tutaj i)
    # istnieje konwencja nadawania nazwy jako znaku podkreślnika (tj. _)
    # Dzięki temu już samo szybkie skanowanie kodu mowi nam ze ta zmienna nie ma znaczenia
    # tj: for _ in range(3)
    for i in range(3):
        wynik+=random.choice(litery)
    for i in range(2):
        wynik+=random.choice(cyfry)
    return wynik

with open('kod.txt','a+') as kod:
    wynik=generuj_kod()
    if wynik in kod.read():
        # no doooooobra, a co jeśli jakimś trafem to wykonanie generuj_kod() zwróci nam wartosc ktora juz zostala
        # wczesniej zapisana / uzyta? Wtedymamy 2x ten sam kod w pliku ;d
        kod.write(generuj_kod()+'\n')
    else:
        kod.write(wynik+'\n')

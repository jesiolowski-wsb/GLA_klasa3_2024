with open('liczby (1).txt','r') as plik: #mam liczby(1) bo jest taki sam plik na komputerze i nie wiem co to nie chce komus czegos zepsuc
    tekst=plik.read()
    lista=tekst.split()
    lista_int=[int(x)for x in lista]
    print(lista_int)
    def na_bin(liczba):
        return bin(liczba)[2:]
    def na_hex(liczba):
        return hex(liczba)[2:]
    def statystyki(lista):
        srednia=sum(lista)/len(lista)
        lista.sort()
        if len(lista)%2!=0:
            n=len(lista)
            if n%2==0:
                mediana=(lista[n//2-1]+lista[n//2])/2
            else:
                mediana=lista[n//2]
        return srednia,mediana
    def tabelka(lista):
        wynik_bin={}
        wynik_hex={}
        for liczba in lista:

#nie zdazylam ladnie wszystkiego zrobic :((
#with open('wyniki_liczby.txt','a+') as wyniki_liczby:
#    wyniki_liczby.write



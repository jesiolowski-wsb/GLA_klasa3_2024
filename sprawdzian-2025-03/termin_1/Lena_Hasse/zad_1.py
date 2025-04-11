# zdobyte punkty: 4/6

# ✅ Poprawne otwarcie pliku wejściowego
# ✅ Próba utworzenia tajnej wiadomości
# ✅ Próba zapisu wyniku do pliku
# ❌ Błąd w liczeniu wielkich liter - funkcja zwiększa licznik tylko raz na słowo, a nie dla każdej wielkiej litery
# ❌ Format zwracanego wyniku nie jest zgodny z wymaganiami (brak informacji o liczbie wielkich liter)
# ❌ Brak sprawdzenia czy słowo ma co najmniej 5 znaków przed pobraniem znaku o indeksie 4

with open('tajny_przekaz.txt','r')as plik:
    tekst=plik.read()
    lista=tekst.split()
    def funkcja(tekst):
        licznik={}
        for slowo in tekst.split():
            for litera in slowo:
                if litera.isupper():
                    if slowo in licznik:
                        licznik[slowo]+=1
                    else:
                        licznik[slowo]=1
        najwieksze=max(licznik, key=licznik.get)
        string=''
        for slowa in lista[9::10]:
            string+=slowa[4]
        return f'{najwieksze},{string}'
    print(funkcja(tekst))
with open('wyniki1.txt.','a+') as wyniki:
    wyniki.write(funkcja(tekst))

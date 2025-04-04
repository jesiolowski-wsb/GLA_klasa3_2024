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

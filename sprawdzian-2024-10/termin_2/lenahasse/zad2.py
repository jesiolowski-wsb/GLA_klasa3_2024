# Zdobyte punkty: 5/5

with open('slowa.txt','r') as plik:
    tekst=plik.read()
lista=tekst.split()

# sprytne, ale we wzorzec wchodzić tu będzie też słowo które ma 'ing' gdzieś w środku (np xxxxingxxxx)
# proponowałbym uzycie word.endswith('ing') lub slowo[-3:] == 'ing'
lista_ing=[word for word in lista if 'ing' in word]
print(lista_ing)
with open('filtred.txt','a+') as wyniki:
    for i in lista_ing:
        wyniki.write(f'{i}\n')
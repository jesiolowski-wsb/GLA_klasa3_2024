with open('slowa.txt','r') as plik:
    tekst=plik.read()
lista=tekst.split()
lista_ing=[word for word in lista if 'ing' in word]
print(lista_ing)
with open('filtred.txt','a+') as wyniki:
    for i in lista_ing:
        wyniki.write(f'{i}\n')
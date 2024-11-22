import random
def generuj_kod():
    litery='qwertyuioplkjhgfdsazxcvbnm'
    cyfry='1234567890'
    wynik=''
    for i in range(3):
        wynik+=random.choice(litery)
    for i in range(2):
        wynik+=random.choice(cyfry)
    return wynik
with open('kod.txt','a+') as kod:
    wynik=generuj_kod()
    if wynik in kod.read():
        kod.write(generuj_kod()+'\n')
    else:
        kod.write(wynik+'\n')

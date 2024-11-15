import random
def generuj_id():
    znaki='ABCDE'
    cyfry='0987654321'
    wynik=''
    for i in range (0,2):
        wynik+=random.choice(znaki)
    for j in range (0,3):
        wynik+=random.choice(cyfry)
    return wynik
nowe_id=generuj_id()
print(nowe_id)
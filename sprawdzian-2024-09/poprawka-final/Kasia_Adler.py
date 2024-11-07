# zadanie 4
def lucky_number(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i > 7:
            print("LuckyNumber")
        elif i % 2 == 0:
            print("Lucky")
        elif i > 7:
            print("Number")
        else:
            print(i)

# zadanie 1
def tablica_mnozenia(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:2}", end=" ")   # dodałam :2 żeby były ładne odstępy
        print()

# zadanie 2
def odwroc_liste(lista):

    if len(lista) <= 1: # warunek bazowy bo po co odwracac 1 znak
        return lista
    return [lista[-1]] + odwroc_liste(lista[:-1])

#test
print(odwroc_liste([1, 2, 3, 4, 5]))
print(odwroc_liste(['a', 'b', 'c']))

# zadanie 3
import random

def gra_w_zgadywanie():
    while True:
        celowa_liczba = random.randint(1, 100)

        print("Zgadnij liczbę od 1 do 100 (lub wpisz 'koniec' aby zakończyć):")
        while True:
            zgadywana_liczba = input("> ")

            if zgadywana_liczba == "koniec":
                print("Dziękuję za grę :) ")
                return
            try:
                liczba = int(zgadywana_liczba)
            except ValueError:
                print("Proszę podać liczbę lub 'koniec' aby zakończyć.")
                continue    #znaczy, że pętla zaczyna się od nowa

            if liczba < celowa_liczba:
                print("za mało!")
            elif liczba > celowa_liczba:
                print("za dużo!")
            else:
                print(f"Brawo! Zgadłeś/aś! Wylosowana liczba to {celowa_liczba}.")
                break

        kolejna_tura = input("Czy chcesz zagrać ponownie? (tak/nie)")
        if kolejna_tura != "tak":
            print("Dziękuję za grę! <3")
            break

gra_w_zgadywanie()

# wynik: 4/4 pkt

# zadanie 2:
# fizz przez 3
#buzz przez 5
#boom przez 7
#fizzbuzz przez 15

# def fizzbuzz(n):
#     for liczba in range(1, n+1):
#         if liczba % 3 == 0 and liczba % 5 == 0:
#             print("FizzBuzz")
#         elif liczba % 3 == 0:
#             print("Fizz")
#         elif liczba % 5 == 0:
#             print("Buzz")
#         elif liczba % 7 == 0:
#             print("Boom")
#         else:
#             print(liczba)
# n = 20
# fizzbuzz(n)


# wynik: 7/7 pkt
# zadanie 1
#float konwertuje liczbe na zmiennoprzecinkowa, tak aby mogly tez byc liczby po przecinku np 3.14
while True:
    komenda = input("Wpisz działanie: ")

    if komenda.lower() == "quit":
        print("Kalkulator zaknięty")
        break

    elementy = komenda.split()
    # można by przemyśleć sposób przyporządkowywania elementów do zmiennych
    # aby kod nie powodował wyjątku np poprzez sprawdzenie ilości elementów w liście
    # po wykonanym split tj np
    # if  len(elementy)==3:
    liczba1 = float(elementy[0])
    operator = elementy[1]
    liczba2 = float(elementy[2])

    if operator == "+":
        wynik = liczba1 + liczba2
    elif operator == "-":
        wynik = liczba1 - liczba2
    elif operator == "*":
        wynik = liczba1 * liczba2
    elif operator == "/":
        if liczba2 == 0:
            wynik = "Error"
        else:
            wynik = liczba1 / liczba2

    # problem z wcięciami - zmienna wynik czasem może nie istnieć
    # można by dać jej jakąś wartość początkową np wynik = None
    print(f"Twój wynik to: {wynik}")



zadanie 2:

# fizz przez 3
#buzz przez 5
#boom przez 7
#fizzbuzz przez 15

def fizzbuzz(n):
    for liczba in range(1, n+1):
        if liczba % 3 == 0 and liczba % 5 == 0:
            print("FizzBuzz")

        elif liczba % 3 == 0:
            print("Fizz")

        elif liczba % 5 == 0:
            print("Buzz")

        elif liczba % 7 == 0:
            print("Boom")

        else:
            print(liczba)


n = 100
fizzbuzz(n)


zadanie 1

#float konwertuje liczbe na zmiennoprzecinkowa, tak aby mogly tez byc liczby po przecinku np 3.14
while True:
    komenda = input("Wpisz działanie: ")

    if komenda.lower() == "quit":
        print("Kalkulator zaknięty")
        break

    elementy = komenda.split()
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



    print(f"Twój wynik to: {wynik}")



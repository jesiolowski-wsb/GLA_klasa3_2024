# wynik: 6/7
#Zad.1
while True:
    a = input("> ")
    a = a.split()
    # sugerowalbym a[0].lower() == "quit":
    if a[0] == "quit":
        break
    # fajny sposób kontroli nad poprawnościa ilosci danych wejsciowych
    if len(a) < 3:
        print("Coś źle zrobiłeś ;(")
        continue
    if a[1] == "+":
        print(int(a[0]) + int(a[2]))
    elif a[1] == "-":
        print(int(a[0]) - int(a[2]))
    elif a[1] == "/":
        print(int(a[0]) / int(a[2]))
    elif a[1] == "*":
        # szkoda że tyle printów - chętniej widziałbym to jako zwrotkę z funkcji
        print(int(a[0]) * int(a[2]))
    else:
        print("Coś źle zrobiłeś ;(")

# wynik: 4/4 pkt
#Zad.2
def fizzbuzz_v2(b):
    for i in range(1, b + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output = "Boom"
        if output == "":
            print(i)
        else: print(output)

fizzbuzz_v2(20)

# wynik: 3/3 pkt
#Zad.3
def rysuj_prostokat(szerokosc, wysokosc):
    for i in range(wysokosc):
        print(szerokosc * "#")

rysuj_prostokat(5, 3)

# wynik: 3/8 pkt
# #Zad.4
def is_palindrome(word):
    # ta linia nie ma wpływu na dalsze wykonanie aplikacji
    # co prawda usuwa spacje, ale przetworzonego stringa nigdzie nie przekazuje
    # to jest powód dla którego drugi przykład nie działa
    word.replace(" ", "")
    word = word.lower()
    for i in range(len(word)):
        # bardzo fajny sposób, tylko że to nie jest rekurencja
        if word[i] != word[-(i + 1)]:
            return False
    return True

print(is_palindrome("Kajak"))
print(is_palindrome("A to idiota"))
print(is_palindrome("k a j j a k"))

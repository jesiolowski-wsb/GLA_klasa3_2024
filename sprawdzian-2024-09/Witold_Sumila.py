# wynik: 4/4 pkt
def fizzbuzz(n):
    for liczba in range(1, n):
        if liczba % 3 == 0 and liczba % 5 == 0:
            print("FizzBuzz")
        elif liczba % 3 == 0:
            print("Fizz")
        elif liczba % 5 == 0:
            print("Buzz")
        elif liczba % 7 ==0:
            print("boom")
        else:
            print(liczba)
fizzbuzz(20)

# wynik: 3/3 pkt
# proponowałbym nazywanie zmiennych w sposób zrozumiały dla czytającego
# m i n może nie być czytelne za 5mcy
def rysuj_prostokat(n,m):
    for i in range(n):
        print('#'*m)

rysuj_prostokat(6,4)

# wynik: 8/8 pkt
def is_palindrome(s):
    s=s.replace(" ", "").lower()
    if len(s)<=1:
        return True
    if s[0]== s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
print(is_palindrome("a to idiota"))
print(is_palindrome("Ka jak"))


# wynik: 6/7
while True:
    dane = input('wpisz dzialanie')
    czesci = dane.split()
    # a moze lepiej dane.lower() == "wyjdz" ?
    if dane =="wyjdz":
        print('wyjscie')
        break
    # strasznie sprytne sprawdzenie czy wejscie jest poprawne! gratki :)
    if len(czesci)!=3:
        print('blad')
        break

    if czesci[1]=='*':
        # zastanawia mnie czy nie byloby lepiej zwrócić wynik z funkcji zamiast
        # strzelać printami na lewo i prawo
        print(int(czesci[0])*int(czesci[2]))
    if czesci[1]=='/':
        print(int(czesci[0])/int(czesci[2]))
    if czesci[1] == '+':
        print(int(czesci[0]) + int(czesci[2]))
    if czesci[1] == '-':
            print(int(czesci[0]) - int(czesci[2]))
# wynik: 6/7 pkt
zasada = 1
# ok, to też zadziała, ale troszke czytelniej byłoby narzucenie po prostu
# while True
while zasada== 1:
    a=input("podaj swoje równanie")
    # nie lepiej byłoby zrobić a.lower()=="quit"?
    if a=="quit":
        break
        # ta linia nigdy się nie wykona - break wychodzi poza blok kodu
        zasada=0
    else:
        lista = a.split()
        # szkoda ze nie sprawdzamy poprawności pobranych parametrow
        # po wpisaniu 2+2 aplikacja się wysypuje
        b = int(lista[0])
        c = int(lista[2])
        if lista[1] == "*":
            print(b * c)
        if lista[1] == "+":
            print(b + c)
        if lista[1] == "-":
            print(b - c)
        if lista[1] == "/":
            # zastanawia mnie czy nie moglibyśmy z funkcji zwrócić wyniku zamiast go
            # printować na ekranie. Byłoby schludniej
            print(b / c)

# wynik: 4/4 pkt
def fizzbuzzv2(n):
    for liczba in range(1, n + 1):
        if liczba % 15 == 0:
            print("FizzBuzz")
        if liczba % 3 == 0:
            print("Fizz")
        if liczba % 5 == 0:
            print("Buzz")
        if liczba % 7 ==0:
           print("Boom")
        else:
            print(liczba)

n=20
fizzbuzzv2(n)

# wynik: 3/3 pkt
def rysuj_prostokat():
 x=int(input("podaj szerokosc"))
 y=int(input("podaj wysokosc"))
 k=0
 while k < y :
     print(x*"#")
     k=k+1
rysuj_prostokat()

# wynik: 8/8 pkt
k=input("sprawdz czy slowo jest palidromem")
def is_palindrome(s):
    s=s.replace(" ", "").lower()
    if len(s)<=1:
        return True
    if s[0]== s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
print(is_palindrome(k))


# wynik: 4/4 pkt
def fizzbuzz_v2(n):
    for liczba in range(1, n):
        if liczba % 3 == 0 and liczba % 5 == 0:
            print("Fizzbuzz")
        elif liczba % 5 == 0:
            print("Buzz")
        elif liczba % 3 == 0:
            print("Fizz")
        elif liczba % 7 == 0:
            print("Boom")
        else:
            print(liczba)
n=100
fizzbuzz_v2(n)

# wynik: 2/3 pkt
def rysuj_prostokat(szerokosc, wysokosc):
    # semantycznie do poprawy - wysokość to tak naprawde szerokosc
    # a szerokosc to wysokosc
    for i in range(szerokosc):
        print('#' * wysokosc)

rysuj_prostokat(11, 5)

# wynik: 8/8 pkt
# choć prawdę mówiąc jesteś 4tą osobą która ma dokładnie takie rozwiązanie
# a to zwraca uwagę
def is_palindrome(s):
    s=s.replace(" ", "").lower()
    if len(s)<=1:
        return True
    if s[0]== s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
print(is_palindrome("saippuakivikauppias"))

# wynik: 7/7 pkt
while True:
    dane = input('dawaj liczbe sigma wiariacie')
    czesci = dane.split()
    if dane =="koniec elo elo":
        print('koniec matmy na dzis bratku')
        break
    elif len(czesci)!=3:
        print('ziomek cos zle wpisales')
        break
    elif czesci[1]=='+':
        print(int(czesci[0])+int(czesci[2]))
    elif czesci[1]=='-':
        print(int(czesci[0])-int(czesci[2]))
    elif czesci[1]=='*':
        print(int(czesci[0])*int(czesci[2]))
    elif czesci[1]=='/':
        print(int(czesci[0])/int(czesci[2]))

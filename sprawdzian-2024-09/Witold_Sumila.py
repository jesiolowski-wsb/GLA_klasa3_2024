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




def rysuj_prostokat(n,m):
    for i in range(n):
        print('#'*m)

rysuj_prostokat(6,4)






def is_palindrome(s):
    s=s.replace(" ", "").lower()
    if len(s)<=1:
        return True
    if s[0]== s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
print(is_palindrome("a to idiota"))











while True:
    dane = input('wpisz dzialanie')
    czesci = dane.split()
    if dane =="wyjdz":
        print('wyjscie')
        break
    if len(czesci)!=3:
        print('blad')
        break

    if czesci[1]=='*':
        print(int(czesci[0])*int(czesci[2]))
    if czesci[1]=='/':
        print(int(czesci[0])/int(czesci[2]))
    if czesci[1] == '+':
        print(int(czesci[0]) + int(czesci[2]))
    if czesci[1] == '-':
            print(int(czesci[0]) - int(czesci[2]))







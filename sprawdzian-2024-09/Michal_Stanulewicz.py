zasada = 1
while zasada== 1:
    a=input("podaj swoje równanie")
    if a=="quit":
        break
        zasada=0
    else:
        lista = a.split()
        b = int(lista[0])
        c = int(lista[2])
        if lista[1] == "*":
            print(b * c)
        if lista[1] == "+":
            print(b + c)
        if lista[1] == "-":
            print(b - c)
        if lista[1] == "/":
            print(b / c)
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

n=int(input("podaj liczbe"))
fizzbuzz(n)

def rysuj_prostokat():

 x=int(input("podaj szerokosc"))
 y=int(input("podaj wysokosc"))
 k=0
 while k < y :
     print(x*"#")
     k=k+1
rysuj_prostokat()

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


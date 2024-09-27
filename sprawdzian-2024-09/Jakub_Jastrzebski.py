#Zad.1
while True:
    a = input("> ")
    a = a.split()
    if a[0] == "quit":
        break
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
        print(int(a[0]) * int(a[2]))
    else:
        print("Coś źle zrobiłeś ;(")

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

#Zad.3
def rysuj_prostokat(szerokosc, wysokosc):
    for i in range(wysokosc):
        print(szerokosc * "#")

rysuj_prostokat(5, 3)

#Zad.4

def is_palindrome(word):
    word.replace(" ", "")
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-(i + 1)]:
            return False
    return True

print(is_palindrome("Kajak"))
print(is_palindrome("A to idiota"))
print(is_palindrome("k a j j a k"))

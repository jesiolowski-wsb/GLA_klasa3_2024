# wynik: 6/8
#
# w rozwiązaniu brakuje .lower() i .replace(" ", "")
# tj. podane w poleceniu przykłady nie zadziałają

def is_palindrome(s):
    lista=[]
    for i in s:
        lista+=[i]
    if len(lista) <=1:
        return True
    # czy zmienna lista jest naprawdę potrzenna?
    # nie wystarczyłoby if s[0] != s[-1]
    if lista[0] !=s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome('kolorki'))
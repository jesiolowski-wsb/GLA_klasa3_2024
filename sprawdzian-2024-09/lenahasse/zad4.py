def is_palindrome(s):
    lista=[]
    for i in s:
        lista+=[i]
    if len(lista) <=1:
        return True
    if lista[0] !=s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome('kolorki'))
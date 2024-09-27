# wynik: 2/4 pkt

def fizzbuzz_v2(n):
    for i in range (1,n+1):
        print(i, end=" ")
        if i%3==0:
         print(i, 'Fizz', end='')
         # tutaj problemem jest wcięcie - IF w IFie tj. linia wykonuje sie
         # tylko w obrębie tych podzielnych przez 3.
         # chyba lepiej do wcięć używac TABów a nie spacji
         if i%5==0:
          print('Buzz', end='')
        print('')
fizzbuzz_v2(20)
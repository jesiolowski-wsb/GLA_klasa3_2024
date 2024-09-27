def fizzbuzz_v2(n):
    for i in range (1,n+1):
        print(i, end=" ")
        if i%3==0:
         print('Fizz', end='')
         if i%5==0:
          print('Buzz', end='')
        print('')
fizzbuzz_v2(20)
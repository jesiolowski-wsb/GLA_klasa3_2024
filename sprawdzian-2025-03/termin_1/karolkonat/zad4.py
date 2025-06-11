fp = open("liczby.txt", 'r')
data = [int(liczba.strip()) for liczba in fp.readlines()]
fp.close

resoults = 'ZAD 4.1\n'
for d in data:
    resoults += f"{d}: {bin(d)}, {hex(d)}\n"

cyfry = [0 for i in range(10)]

for d in data:
    for c in str(d):
        cyfry[int(c)] += 1

data.sort()
cyfry = {i:cyfry[i] for i in range(len(cyfry)) if cyfry[i] != 0}
mediana =  (data[len(data)//2] + data[len(data)//2+1])/2 if len(data)%2 == 0 else data[len(data)//2] 
# uwielbiam nieczytelne f-stringi
resoults += f"\n\nZAD 4.2\nŚrednia: {sum(data)/2}\nMediana: {data[len(data)//2]}\nWystąpienia cyfr: {cyfry}\n"

fp = open("wyniki_liczby.txt", 'w')
fp.write(resoults)
fp.close()

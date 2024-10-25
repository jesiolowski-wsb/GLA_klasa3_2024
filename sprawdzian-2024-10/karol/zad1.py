def convert(n):
	tmp = ''
	while n > 0:
		tmp += str(n%2)
		n = n//2

	return tmp[::-1]



data = []
fp = open('liczby.txt', 'r')
data = [int(a) for a in fp.readlines()]
fp.close()

resoult = ''

for d in data:
	resoult += f"{d}: {convert(d)}\n"

fp = open('wyniki.txt', 'w')
fp.write(resoult)
fp.close()
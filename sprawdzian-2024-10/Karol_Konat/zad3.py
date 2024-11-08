# Zdobyte punkty: 5/4

# ej no... to się nudne robi... kolejny komplement dla Ciebie
# fajny sposób importowania tylko tego, czego potrzebujemy!
from random import randint, choice

LETTERS = "ABCDEFGHIJKLMNOPRSTUWVQXYZ"


def generuj_id():
	id = choice(LETTERS)+choice(LETTERS)+str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
	fp=open('id.txt', 'w')
	fp.write(id)
	fp.close()
	return(id)

nowe_id = generuj_id()
print(nowe_id)
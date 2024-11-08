# Zdobyte punkty: 5/5
fp = open("tekst.txt", 'r')
text = fp.read()
fp.close()

# w tym wypadku to nadmiarowe, ale rozumiem potrzebę
text = text.replace('\n', ' ')

l = [wrd for wrd in text.split() if len(wrd) > 3 and wrd[0].isupper()]
fp = open("analiza.txt", 'w')
# no dobra, ale to akurat mega swiadome uzycie joina serio mega
# also: chyba musze przestac Cie tylko chwalic :D
fp.write('\n'.join(l))
fp.close()
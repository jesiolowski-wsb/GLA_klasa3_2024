fp = open("teskt.txt", 'r')
text = fp.read()
fp.close()

text = text.replace('\n', ' ')

l = [wrd for wrd in text.split() if len(wrd) > 3 and wrd[0].isupper()]
fp = open("analiza.txt", 'w')
fp.write('\n'.join(l))
fp.close()
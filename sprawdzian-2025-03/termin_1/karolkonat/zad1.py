fp = open("tajny_przekaz.txt")
data = [l.strip() for l in fp.readlines()]
fp.close

max_caps = 0
max_caps_word = ''
secret = ''
for i in range(len(data)):
    caps = len([c for c in list(data[i]) if c.isupper()])
    if caps > max_caps:
        max_caps_word = data[i]
        max_caps = caps
    if (i+1)%10 == 0:
        secret+=data[i][4]

fp = open("wyniki1.txt", 'w')
fp.write(f"ZAD 1.1\n{max_caps_word} ({max_caps})\n\nZAD1.2\n{secret}\n")
fp.close()

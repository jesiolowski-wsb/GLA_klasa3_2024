fp  = open('dane.txt', 'r')
lines = fp.read()
lines = lines.split('\n')
fp.close

dec_d = [str(int(l, base=2)) for l in lines if l[-1]=='0']


fp = open('wyniki.txt', 'w')
fp.write('\n'.join(dec_d))
fp.close()
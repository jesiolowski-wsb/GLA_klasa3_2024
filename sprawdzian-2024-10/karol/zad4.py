fp  = open('dane.txt', 'r')
lines = fp.readlines()
fp.close

dec_d = [str(int(l, base=2)) for l in lines if int(l, base=2)%2==0]


fp = open('wyniki.txt', 'w')
fp.write('\n'.join(dec_d))
fp.close()
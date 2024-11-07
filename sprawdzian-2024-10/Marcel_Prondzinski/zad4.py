# Zdobyte punkty: 7/7
# strasznie fajne i zwięzłe! Co prawda nazwa zmiennej bez sensu, ale rozumiem że to już Twoja estetyka

sigmaligmadigma  = open('dane.txt', 'r')
lines = sigmaligmadigma.readlines()
sigmaligmadigma.close
dec_d = [str(int(l, base=2)) for l in lines if int(l, base=2)%2==0]
sigmaligmadigma = open('wyniki.txt', 'w')
sigmaligmadigma.write('\n'.join(dec_d))
sigmaligmadigma.close()

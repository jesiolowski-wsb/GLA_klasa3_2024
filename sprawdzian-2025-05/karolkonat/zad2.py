def NWD(a, b):
	a = abs(a)
	b = abs(b)

	if b == 0:
		return a
	if a == 0:
		return b
	return NWD(b, a%b)

def NWW(a, b):
	a = abs(a)
	b = abs(b)
	return int((a*b)/NWD(a,b))

print(NWD(12, 18))  # 6
print(NWD(35, 14))  # 7
print(NWD(13, 7))   # 1

print(NWW(12, 18))  # 36
print(NWW(6, 8))    # 24
print(NWW(7, 13))   # 91
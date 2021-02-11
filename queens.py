ls = [1,2,3,4,5,6,7,8]
def diag(ls):
	for i in ls:
		for j in ls:
			if i != j:
				if abs(i - j) == abs(ls[i - 1] - ls[j - 1]):
					return True
					break 
	return False

# def Q(op, save = []):
# 	fulllist = []
# 	if len(op) == 1:
# 		final = save + op
# 		if not diag(final):
# 			print(final)
# 			return 0
# 		return 0
# 	for i in range(len(op)):
# 		pasrecurs = save[:]
# 		pasrecurs.append(op[i])
# 		pasop = op[:i] + op[i+1:]
# 		Q(pasop, pasrecurs)
# Q(ls)
# 
ls2 = [1,2,3]

def TQ(op, save = [], allper = []):
	if len(op) == 1:
		final = save + op
		allper.append(final)
		return allper
	for i in range(len(op)):
		pasrecurs = save[:]
		pasrecurs.append(op[i])
		pasop = op[:i] + op[i+1:]
		allper = TQ(pasop, pasrecurs, allper)
	return allper

print(TQ(ls2))

def isPrime(n,j):
    if (n == 0 or n == 1):
        return False
 
    if (n == j):
        return True
 
    if (n % j == 0):
        return False
 
    j += 1
 
    return isPrime(n, j)

i = 100
primeList = []

while True:
	check = i // 100
	if check < 1:
		continue
	elif check > 9:
		break
	else:
		if isPrime(i,2):
			primeList.append(i)
	i += 1

print(primeList)

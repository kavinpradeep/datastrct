def findmaxprime(number):
	i=1
	maxPrime=i
	while number!=1:
		i+=1
		while number%i==0:
			number/=i
			maxPrime=i
	return maxPrime	

print(findmaxprime(9))
print(findmaxprime(11))
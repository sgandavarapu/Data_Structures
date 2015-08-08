#Write a script to compute how many unique prime factors an integer has.  
#For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3. 
#Use your script to compute the number of unique prime factors of 1234567890

def uniq_factors(n):
	answer =[]
	i=2
	while i<= n:
		if n%i ==0:
			n = n/i
			if i not in answer:
				answer.append(i)
			i=1
		i=i+1
	return len(answer)

n = int(input())
print uniq_factors(n)
#Write a script that prompts the user for their phone number, x. Then carry out the following steps:
 #1. Compute x minus the sum of the digits of x. Call this result y. 
 #(hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
#2. Compute the sum of the digits of y, and store the result back in y.
#3. Repeat step 2 until y has just one digit, then display it.
 
#What answer do you get?

def digitsSum(x):
	a=x//10
	b=x%10
	while a>=10:	
		b = b + a%10
		a = a//10
	return b+a

x = int(input())
y = x - digitsSum(x)
while y >=10:
	y = digitsSum(y)
print y	
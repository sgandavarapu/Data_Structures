#Write a script that prompts the user for an integer tree size, then displays a number tree, as shown below:
#5
#    1
#   121
#  12321
# 1234321
#123454321

x = int(input())
out = [' ']*x
#print ''.join(out)
for i in range(1,x+1):
	k=0
	for j in range(i,0,-1):
		out[x-1-k] = str(j)
		k=k+1
	out2 = out[::-1][1:]
	out = out + out2
	print ''.join(out)
	out = [' ']*x





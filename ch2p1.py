
import math

def interleave(text1,text2):
	out=[]
	n = len(text1)
	for i in range(0,n):
		out.append(text1[i]+text2[i])
	return ''.join(out)

def scramble(text,num):
	n=len(text)
	curr_num = num
	if n==curr_num:
		return interleave(str(text[:n/2]),str(text[n/2:]))
	else:
		return scramble(text[:n/2],curr_num) + scramble(text[n/2:],curr_num)

def process(str):
	l = len(in_str)
	for i in range(1,l):
		if pow(2,i)>=l:
			n=pow(2,i)-l
			break
		else:
			continue
	return in_str+(' '*n)

def geom_prog(l,m):
	#return a list of numbers with gemetric progression with ratio m, till number l
	elements=[]
	for i in range(m,l): # prepare a list with geometric progresssion of 2.
		if pow(m,i)<=l:
			elements.append(pow(m,i))
		else:
			break
	return elements

in_str= str(input())
in_str = process(in_str) #make sure string is of length pow(2)
#print len(in_str)
elements= geom_prog(len(in_str),2) # obtain list of geom progression
#print elements
for i in elements:
	in_str = scramble(in_str,i)
print in_str

#Message #1:
#Madam I'm Adam.
#We demand rigidly defined areas of doubt and uncertainty!
#The illusion of self-awareness. Happy automatons, running on trivial programs. I'll bet you never guess. From the inside, how can you?

#12345678

#1234 5678

#12 34 56 78

#1324 5768

#15372648
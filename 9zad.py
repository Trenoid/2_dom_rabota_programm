k=int(input())
s=[]
while k>0:
	ost=k%2
	k=k//2
	s.append(str(ost))
s.reverse()
print("".join(s))
	

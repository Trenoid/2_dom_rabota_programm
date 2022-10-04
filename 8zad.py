k=int(input())
dlina=len(str(k))
s=0
for i in range(1,dlina+1):
	rag=10**(dlina-i)
	tre=k//rag
	s+=tre*2**(dlina-i)
	k=k-tre*10**(dlina-i)
print(s)
	
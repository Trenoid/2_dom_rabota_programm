k=int(input())
dlina=len(str(k))

for i in range(1,dlina+1):
	rag=10**(dlina-i)
	tre=k//rag
	gad=tre*10**(dlina-i)
	print(gad)
	k=k-tre*10**(dlina-i)
	
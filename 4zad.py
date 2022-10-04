x=float(input())
y=float(input())
l=0.5**(x**2+y**2)
for i in range(1,10+1):
	if l<=i:
		print(i)
		break
if l>10:
	print("missed")

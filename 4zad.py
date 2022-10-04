x=float(input())
y=float(input())
l=(x**2+y**2)**0.5
for i in range(1,10+1):
	if l<=i:
		print(i)
		break
if l>10:
	print("missed")

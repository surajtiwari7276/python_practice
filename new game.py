p1=input("what you want")
p2=input("whatyou want")

if p1=="paper" or p1=="scissors" or p1=="rock":

	if p1==p2:
		print("its a tie")

	if p1=="rock":
		if p2=="scissors":
			print("p1 wins")
		elif p2=="paper":	
			print("p2 wins")

	if p1=="paper":
		if p2=="scissors":
			print("p2 wins")
		elif p2=="rock":	
			print("p1 wins")

	if p1=="scissors":
		if p2=="paper":
			print("p1 wins")
		elif p2=="rock":	
			print("p2 wins")
else:
	print("something went wrong")
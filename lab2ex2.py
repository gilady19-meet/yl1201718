abc = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []
 
def myFunction():
	for i in abc:
		if (i<5):
			print (i)

myFunction()

def new():
	for i in abc:
		if (i<5):
			list2.append(i)
	print (list2)


new()
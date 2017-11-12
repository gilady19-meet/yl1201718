import turtle
turtle.addshape("oGEOJ2JU.gif")
turtle.getshapes()
turtle.shape("oGEOJ2JU.gif")
a=20
turtle.speed(5000)
for i in range (500):
	turtle.forward(270)
	turtle.right(50)
	turtle.forward(170)
	turtle.right(100)
	turtle.forward(130)
	turtle.home()
	turtle.right(a)
	a=a+1
turtle.mainloop()
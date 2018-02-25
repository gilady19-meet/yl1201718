import turtle
import math
import time
import random
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)
turtle.bgpic("realmadrid.gif")
turtle.setup(1280 , 720)
RUNNING = True;
SLEEP=0.0077;
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)



MY_BALL=Ball(0,0, 0 , 0, 50, "lightblue")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = int(MY_BALL.radius*0.75)
MAXIMUM_BALL_RADIUS = int(MY_BALL.radius*1.5)
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3
MINIMUM_BALL_DY = -3
MAXIMUM_BALL_DY = 3
SCORE=0

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	while MY_BALL.distance(x,y) < MY_BALL.radius*2:
		x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
	ball = Ball(x , y, dx ,dy, radius , color)
	BALLS.append(ball)


def move_all_balls():
	for i in range(len(BALLS)):
		BALLS[i].move(SCREEN_WIDTH , SCREEN_HEIGHT)


def collide(ball_a, ball_b):
	if ball_a==ball_b:
		return False
	d = math.sqrt(math.pow((ball_a.xcor()- ball_b.xcor() ),2) + math.pow((ball_a.ycor() - ball_b.ycor()),2))
	if d+10<=int(ball_a.radius)+int(ball_b.radius):
		return True
	else:
		return False


def  check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			a=collide(ball_a,ball_b)
			if a==True:
				ra=ball_a.radius
				rb=ball_b.radius
				x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) ,  int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while dx==0:
					dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while dy==0:
					dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius=random.randint(int(MY_BALL.radius*0.75), int(MY_BALL.radius*1.5))
				color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
				if ra<rb:
					ball_a.goto(x, y) 
					ball_a.dx=dx
					ball_a.dy=dy 
					ball_a.radius=radius
					ball_a.color(color)
					ball_b.radius+=1
					ball_b.shapesize(int(ball_b.radius/10))
					ball_a.shapesize(int(ball_a.radius/10))

				if ra>rb:
					ball_b.goto(x, y) 
					ball_b.dx=dx
					ball_b.dy=dy 
					ball_b.radius=radius
					ball_b.color(color)
					ball_a.radius+=1
					ball_a.shapesize(int(ball_a.radius/10))
					ball_b.shapesize(int(ball_b.radius/10))
def win():
	text = turtle.clone()
	text.ht()
	text.write("you are too big, you won", align = "center", font = ("lklug",50,"bold"))
	time.sleep(4)
	quit()

def lose():
	text = turtle.clone()
	text.ht()
	text.write("you lost", align = "center", font = ("lklug",50,"bold"))
	time.sleep(4)
	# quit()	


newscore = turtle.clone()
def check_myball_collision():
	global SCORE
	for otherball in BALLS:	
		a=collide(otherball,MY_BALL)
		if a==True:
			rob=otherball.radius
			rmb=MY_BALL.radius
			if rmb<rob:
				print(otherball)
				print(MY_BALL)
				lose()
				return False
			elif rmb>rob:
				SCORE += 1
				newscore.clear()
				newscore.penup()
				newscore.goto(0 , SCREEN_HEIGHT-100)
				newscore.write("score: " + str(SCORE), align = "center", font = ("lklug",20,"bold"))
				x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while dx==0:
					dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while dy==0:
					dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius=random.randint(int(MY_BALL.radius*0.75), int(MY_BALL.radius*1.5))
				color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
				otherball.goto(x, y) 
				otherball.dx=dx
				otherball.dy=dy 
				otherball.radius=radius
				otherball.color(color)
				otherball.shapesize(int(otherball.radius/10))
				MY_BALL.radius+=int(otherball.radius/7)
				MY_BALL.shapesize(MY_BALL.radius/10)
				if MY_BALL.radius >= 200:
					win()
	return True

def movearound(event):
	MY_BALL.x=event.x-SCREEN_WIDTH 
	MY_BALL.y=SCREEN_HEIGHT - event.y
	MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING == True:
	if SCREEN_WIDTH !=turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
	if SCREEN_HEIGHT !=turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	move_all_balls()
	turtle.getscreen().update()
	check_all_balls_collision()
	turtle.getscreen().update()
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()















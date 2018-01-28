import turtle
import math
import time
import random
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)

RUNNING = True;
SLEEP=0.0077;
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)


MY_BALL=Ball(0,0, 10 , 10, 15, "blue")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]

for i in range(5):
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
	for ball in BALLS:
		ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)


def collide(ball_a, ball_b):
	if ball_a==ball_b:
		return False
	d = math.sqrt(math.pow((ball_a.x- ball_b.x ),2) + math.pow((ball_a.y - ball_b.y),2))
	if d+10<=ball_a.radius+ball_b.radius:
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
				radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
				if ra<rb:
					ball_a.goto(x, y) 
					ball_a.dx=dx
					ball_a.dy=dy 
					ball_a.radius=radius
					ball_a.color(color)
					ball_b.radius+=1
					ball_b.shapesize(radius/10)

				if ra>rb:
					ball_b.goto(x, y) 
					ball_b.dx=dx
					ball_b.dy=dy 
					ball_b.radius=radius
					ball_b.color(color)
					ball_a.radius+=1
					ball_a.shapesize(radius/10)

def check_myball_collision():
	for otherball in BALLS:	
		a=collide(otherball,MY_BALL)
		if a==True:
			rob=otherball.radius
			rmb=MY_BALL.radius
			if(rmb<rob):
				return False
			else:
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
				otherball.goto(x, y) 
				otherball.dx=dx
				otherball.dy=dy 
				otherball.radius=radius
				otherball.color(color)
				MY_BALL.radius+=1
				MY_BALL.shapesize(radius/10)
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
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()















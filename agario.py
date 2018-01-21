import turtle
import time
import random
from ball import Ball
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)

RUNNING = True;
SLEEP=0.0077;
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0, 10 , 10, 15, "blue")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX =5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]

for i in range(5):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
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
	d = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
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
				x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
				if ra<rb:
					ball_a(x, y, dx ,dy , radius , color)
				if ra>rb:
					ball_B(x, y, dx ,dy , radius , color)
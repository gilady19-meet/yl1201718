def fatcollide(shooting, fat_zombe):
	if shooting==fat_zombe:
		return False
	d = math.sqrt(math.pow((shooting.xcor()- fat_zombe.xcor() ),2) + math.pow((shooting.ycor() - fat_zombe.ycor()),2))
	if d+10<=int(fat_zombe.radius)+int(shooting.radius):
		return True
	else:
		return False


def zombie_shoot_collision():
	for fat_zombe in zombie_list:	
		c=collide(shooting, fat_zombe)
		if c==True:
			zombie_list.pop(fat_zombe)
	return True

def fastcollide(shooting, fast_zombe):
	if shooting==fast_zombe:
		return False
	d = math.sqrt(math.pow((shooting.xcor()- fast_zombe.xcor() ),2) + math.pow((shooting.ycor() - fast_zombe.ycor()),2))
	if d+10<=int(fast_zombe.radius)+int(shooting.radius):
		return True
	else:
		return False


def zombie_shoot_collision():
	for fast_zombe in zombie_list:	
		c=collide(shooting, fast_zombe)
		if c==True:
			zombie_list.pop(fasbt_zombe)
	return True
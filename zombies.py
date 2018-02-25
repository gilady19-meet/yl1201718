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
import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
ragolo.hideturtle()
ragolo.tracer(False)
turtle.update()

#setup
ragolo.left(180)
ragolo.penup()
ragolo.forward(450)
ragolo.right(90)
ragolo.forward(250)
ragolo.pendown()
ragolo.right(90)

def move(depth, size=243):
	
	if depth > 1:
		move(depth-1, size/3)
		ragolo.left(60)
		move(depth-1, size/3)
		ragolo.right(120)
		move(depth-1, size/3)
		ragolo.left(60)
		move(depth-1, size/3)
		
	if depth == 1:
		ragolo.forward(size)
		ragolo.left(60)
		ragolo.forward(size)
		ragolo.right(120)
		ragolo.forward(size)
		ragolo.left(60)
		ragolo.forward(size)
		
	turtle.update()
		

while True:
	conversionWorked = 0
	plsend = 0
	while not conversionWorked:
		depth = raw_input("Please enter a depth level [q to quit]\n> ")
		
		conversionWorked = 1
		
		if str(depth) == 'q':
			plsend = 1
			break
		
		try:
			depth = int(depth)
		except ValueError:
			conversionWorked = 0
		
		if depth < 1 or depth > 6:
			conversionWorked = 0
	
	if plsend:
		break
	
	move(depth)
	ragolo.right(120)
	move(depth)
	ragolo.right(120)
	move(depth)
	ragolo.right(120)

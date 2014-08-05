import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
ragolo.tracer(False)
turtle.update()

#setup
ragolo.left(180)
ragolo.penup()
ragolo.forward(450)
ragolo.left(90)
ragolo.forward(250)
ragolo.pendown()
ragolo.left(90)
ragolo.left(60)

def drawTrig(size):
	ragolo.forward(size)
	ragolo.right(120)
	ragolo.forward(size)
	ragolo.right(120)
	ragolo.forward(size)
	ragolo.right(120)
	turtle.update()

def move(depth, size=729):
	
	if depth > 1:
		move(depth-1, size/2)
		
		ragolo.penup()
		ragolo.forward(size/2)
		ragolo.pendown()
		
		move(depth-1, size/2)
		
		ragolo.penup()
		ragolo.right(120)
		ragolo.forward(size/2)
		ragolo.left(120)
		ragolo.pendown()
		
		move(depth-1, size/2)
		
		ragolo.penup()
		ragolo.left(120)
		ragolo.forward(size/2)
		ragolo.right(120)
		ragolo.pendown()
		
	if depth == 1:
		drawTrig(size)
		

while True:
	conversionWorked = 0
	plsend = 0
	while not conversionWorked:
		depth = raw_input("Please enter a depth level [q to quit]\n> ")

		if str(depth) == 'q':
			plsend = 1
			break

		conversionWorked = 1

		try:
			depth = int(depth)
		except ValueError:
			conversionWorked = 0
		
		if depth < 1:
			conversionWorked = 0
	
	if plsend:
		break
	
	move(depth)
	

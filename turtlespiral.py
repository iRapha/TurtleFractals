import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)

#setup
ragolo.penup()
ragolo.backward(300)
ragolo.left(90)
ragolo.backward(300)
ragolo.right(90)
ragolo.left(1)
ragolo.pendown()

def move(depth, size=600):
	ragolo.forward(size)
	ragolo.left(91)
	
	if depth > 1:
		move(depth-1, size-5)
		
	if depth == 1:
		ragolo.hideturtle()

while True:
	conversionWorked = 0
	plsend = 0
	while not conversionWorked:
		depth = raw_input("Please enter a depth level [try 120 | q to quit]\n> ")
		
		conversionWorked = 1
		
		if str(depth) == 'q':
			plsend = 1
			break
		
		try:
			depth = int(depth)
		except ValueError:
			conversionWorked = 0
		
		if depth < 1:
			conversionWorked = 0
	
	if plsend:
		break
	
	move(depth)

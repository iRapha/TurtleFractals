import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
ragolo.hideturtle()
ragolo.tracer(False)

#setup
ragolo.penup()
ragolo.backward(500)
ragolo.left(90)
ragolo.backward(500)
ragolo.right(90)
ragolo.pendown()

def move(depth, size=300):

	ragolo.penup()
	ragolo.forward(size)
	ragolo.left(90)
	ragolo.forward(size)
	ragolo.right(90)
	ragolo.pendown()
	
	ragolo.forward(size)
	ragolo.left(90)
	ragolo.forward(size)
	ragolo.left(90)
	ragolo.forward(size)
	ragolo.left(90)
	ragolo.forward(size)
	ragolo.left(90)
	
	ragolo.penup()
	ragolo.backward(size)
	ragolo.left(90)
	ragolo.backward(size)
	ragolo.right(90)
	ragolo.pendown()
	
	if depth > 1:
	
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.forward(size)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.forward(size)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.left(90)
		ragolo.forward(size)
		ragolo.right(90)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.left(90)
		ragolo.forward(size)
		ragolo.right(90)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.left(180)
		ragolo.forward(size)
		ragolo.right(180)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.left(180)
		ragolo.forward(size)
		ragolo.right(180)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.right(90)
		ragolo.forward(size)
		ragolo.left(90)
		ragolo.pendown()
		
		move(depth-1, size/3)
		
		ragolo.penup()
		ragolo.right(90)
		ragolo.forward(size)
		ragolo.left(90)
		ragolo.pendown()
		
		
	if depth == 1:
		return

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
		
		if depth < 1:
			conversionWorked = 0
	
	if plsend:
		break
	
	move(depth)

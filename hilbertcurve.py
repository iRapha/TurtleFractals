import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
ragolo.hideturtle()
ragolo.tracer(False)
turtle.update()

#setup
ragolo.penup()
ragolo.backward(450)
ragolo.left(90)
ragolo.backward(450)
ragolo.right(90)
ragolo.pendown()

def move(depth, size=900.0):
	
	if depth > 1:
	
		#calculating new size
		over = 1
		under = 3
		for i in range(depth-2):
			over = under
			under = (under*2) + 1 
		
		ragolo.penup()
		ragolo.left(90)
		ragolo.forward(size*over/under)
		ragolo.right(180)
		ragolo.pendown()
		
		move(depth-1, size*over/under)
		
		ragolo.left(180)
		ragolo.forward(size/under)
		ragolo.right(90)
		
		move(depth-1, size*over/under)
		
		ragolo.penup()
		ragolo.forward(size*over/under)
		ragolo.pendown()
		ragolo.forward(size/under)
		
		move(depth-1, size*over/under)
		
		ragolo.penup()
		ragolo.forward(size*over/under)
		ragolo.right(90)
		ragolo.pendown()
		ragolo.forward(size/under)
		ragolo.up()
		ragolo.forward(size*over/under)
		ragolo.right(180)
		ragolo.pendown()
		
		move(depth-1, size*over/under)
		
		ragolo.penup()
		ragolo.right(90)
		ragolo.backward(size)
		ragolo.pendown()
		
		#print str(over) + "\\" + str(under) + "\n\n"
		
	if depth == 1:
		ragolo.penup()
		ragolo.forward(size)
		ragolo.left(90)
		ragolo.pendown()
	
		ragolo.forward(size)
		ragolo.left(90)
		ragolo.forward(size)
		ragolo.left(90)
		ragolo.forward(size)
		ragolo.left(90)
		
		turtle.update()

while True:
	conversionWorked = 0
	plsend = 0
	while not conversionWorked:
		depth = raw_input("Please enter a depth level [1-10 | q to quit]\n> ")
		
		conversionWorked = 1
		
		if str(depth) == 'q':
			plsend = 1
			break
		
		try:
			depth = int(depth)
		except ValueError:
			conversionWorked = 0
		
		if depth < 1 or depth > 10:
			conversionWorked = 0
	
	if plsend:
		break
	
	move(depth)

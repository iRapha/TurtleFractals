import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
# uncomment this for high depth levels
# ragolo.tracer(False)
ragolo.hideturtle()
turtle.update()

#setup
ragolo.right(90)
ragolo.penup()
ragolo.forward(450)
ragolo.pendown()
ragolo.left(180)

def move(depth, size=200):
	
	ragolo.forward(size)
	
	if depth > 1:
		ragolo.left(30)
		move(depth-1, 4*size/5)
		ragolo.backward(4*size/5)
		ragolo.right(60)
		move(depth-1, 4*size/5)
		ragolo.backward(4*size/5)
		ragolo.left(30)
		
	if depth == 1:
		turtle.update()
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
	ragolo.backward(200)

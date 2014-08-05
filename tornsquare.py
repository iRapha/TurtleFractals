import turtle

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(10)
ragolo.hideturtle()
ragolo.tracer(False)

#setup
ragolo.penup()
ragolo.backward(450)
ragolo.left(90)
ragolo.backward(450)
ragolo.right(90)
ragolo.pendown()

def move(depth, size=900.0):
	
	if depth > 0:
	
		#calculating new size
		over = 7
		under = 15
		for i in range(depth-2):
			over = under
			under = (under*2) + 1 
		
		move(depth-1, size*over/under)
		ragolo.left(88)
		move(depth-1, size*over/under)
		ragolo.right(88+88)
		move(depth-1, size*over/under)
		ragolo.left(88)
		move(depth-1, size*over/under)
		
		
	if depth == 0:
		ragolo.forward(size)
		

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
		
	for i in range(4):
		move(depth)
		ragolo.left(90)
	
	turtle.update()

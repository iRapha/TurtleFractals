import turtle
import math

turtle.setup(1100, 1100)
ragolo = turtle.Turtle()
ragolo.speed(0)
ragolo.tracer(False)
ragolo.backward(300)
ragolo.hideturtle()
turtle.update()

def move(depth, size, currentangle=0):
	
	if depth == 0:
		ragolo.forward(size)
		return currentangle
	else:
		size = math.sqrt(2) * size/2
		currentangle += 45
		ragolo.left(currentangle)
		
	
	#sequence maker
	seq = [1]
	
	for i in range(depth-1):
		seq += [1] + map(lambda x: not x, seq[::-1])
		size = math.sqrt(2) * size / 2
	
	for instruction in seq:
		ragolo.forward(size)
		(ragolo.right if instruction else ragolo.left)(90)
	ragolo.forward(size)
	
	turtle.update()
	
	return currentangle

while True:
	curangle = 0
	plsend = 0
	
	for i in range(0, 19):
		# 19 is MAX WITHOUT CRASHING.
		
		curangle = move(i, 600, curangle)
		
		#setup
		ragolo.penup()
		ragolo.setx(0)
		ragolo.sety(0)
		ragolo.seth(0)
		ragolo.backward(300)

		press = raw_input("[keep pressing enter | q to quit]\n> ")
		
		if str(press) == 'q':
			plsend = 1
			break
		
		ragolo.pendown()
		ragolo.clear()
		
	if plsend:
		break
	

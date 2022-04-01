import turtle
import time
import random

#Constant values always in caps
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
	racers = 0
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric... Try Again')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number not in range 2-10. Try again! ')

def race(colors):
	#we need to know the colour of each turtle so we assign creation of turtles to the variable to be stored
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			#Randomly generates a number between 1 and 20 to move it that many pixels
			distance = random.randrange(1, 20)
			racer.forward(distance)
			#To check if the turtles have crossed the finish line:
			#gives the position of the turtles through x and y axis values
			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				#Getting the turtle number from the list to know the colour
				return colors[turtles.index(racer)]


def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	#enumerate - gives index and value of all colors in the list
	#['red', 'blue'] - 1st(i == 0, color == red), 2nd(i == 1, color == blue)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		#default arrows to the right so we need to turn it upto 90 degrees left to go up
		racer.left(90)
		racer.penup()
		#Setting the position of racer through setpos method(takes x and y value)
		#Since the spacing of turtles need to be equal near the bottom and according to the numbers it will vary,
		# We use negative to put at the bottom. We take the width of the screen and divide by no.of turtles+1 (WHY ? Because the turtles need to be spaced as equally off from the screen as well)
		#Y axis is height based after comma
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
#Select random colours according to number of racers given
colors = COLORS[:racers]

winner = race(colors)
print(winner)
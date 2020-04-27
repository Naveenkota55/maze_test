import turtle

wn=turtle.Screen();
wn.bgcolor("white");
wn.title("maze");
wn.setup(700,700);

class Pen1(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("black")
		self.penup()
		self.speed(0)
	
levels=[""]

level_1= [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXXXXXXXXXXXXXXX XX",
"X XXXXXXXX        XXXX XX",
"X                 XXXX XX",
"X                 XXXX XX",
"X                 XXXX XX",
"X XXXX XX                ",
"X                      XX",
"               XXXXXXXXX"
]

levels.append(level_1)

def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			character = level[y][x]
			screen_x= -288 + (x * 24)
			screen_y= 288 - (y* 24)
			
			if character == "X":
				pen.goto(screen_x,screen_y)
				pen.stamp()

pen=Pen1()

setup_maze(levels[1])





import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named spider
lucas = turtle.Turtle()
lucas.speed(0)

def draw_tooth(size):
  lucas.fillcolor('red')
  lucas.begin_fill()
  for _ in range(3):
      lucas.forward(size)
      lucas.right(120)
  lucas.end_fill()

# Draw the body
def flatoval(r):               
  lucas.right(45)
  for loop in range(2):
      lucas.circle(r,90)
      lucas.circle(r/1.5,90)
      

def draw_leg(size):
  turtle.right(45)
  lucas.forward(70)

lucas.penup()
lucas.goto(-68,0)
lucas.pendown()
lucas.pensize(15)
flatoval(130)
lucas.left(45)
lucas.penup()
lucas.forward(50)
lucas.pendown()
lucas.pensize(10)
lucas.right(35)
lucas.circle(70, 70)
lucas.pensize(1)


lucas.backward(15)
lucas.right(5)
draw_tooth(15)
lucas.penup()
lucas.right(35)
lucas.backward(68)
lucas.pendown()
lucas.right(20)
draw_tooth(15)


# Draw the legs
legs = 8
def leg():
  lucas.left(45)
  lucas.forward(100)
  lucas.left(-45)
  lucas.forward(100)

for j in range(-2, 2, 3):
  for i in range(4):
      lucas.penup()
      print(j)
      lucas.goto(j* 139, 50 + 15*i)
      lucas.pendown()
      lucas.pensize(4)
      leg()
lucas.penup()
lucas.goto(-30,70)
lucas.pendown()
lucas.dot(20, "orange")

lucas.penup()
lucas.goto(75,70)
lucas.pendown()
lucas.dot(20, "orange")

# # Hide the turtle and display the window
lucas.hideturtle()
# turtle.done()

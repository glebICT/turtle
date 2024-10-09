import turtle

# Set up the turtle
turtle.speed(0)  # Fastest drawing speed

turtle.pensize(2)  # Set pen size

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)

# Function to draw a circle with a specific color
def draw_circle(radius):
    turtle.circle(radius)

# Function to draw the mandala pattern
def draw_mandala(repeats, size):
    for i in range(repeats):
        # Draw shapes in the mandala
        draw_square(size)
        draw_circle(size / 2)
        draw_triangle(size)
        
        # Rotate for the next segment
        turtle.right(360 / repeats)

# Position the turtle for drawing
turtle.penup()
turtle.goto(0, -100)  # Move to starting position
turtle.pendown()

# Draw the mandala with specified repeats and size
draw_mandala(12, 50)  # 12 segments, size of shapes is 50

turtle.hideturtle()  # Hide the turtle at the end
turtle.done()  # Finish drawing

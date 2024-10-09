import turtle
# Function to draw a Y shape recursively
def y(sz, level):
    if level > 0:
        turtle.pencolor(0, 255 // level, 0)
        turtle.forward(sz)  # Draw the base of the Y
        turtle.right(30)     # Turn right for the right branch
        y(0.8 * sz, level - 1)  # Recursive call for right branch
        turtle.left(60)      # Turn left for the left branch
        y(0.8 * sz, level - 1)  # Recursive call for left branch
        turtle.right(30)     # Reset direction
        turtle.backward(sz)  # Go back to the base of the Y

# Start drawing the fractal tree
turtle.right(-90)  # Face upwards
y(80, 7)           # Draw a Y tree of size 80 and depth 7

turtle.done() 

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# List of colors
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Draw a spiral pattern
for i in range(5000):
    pen.color(random.choice(colors))
    pen.forward(i * 2)
    pen.right(91)  # Slightly more than 90 degrees

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()

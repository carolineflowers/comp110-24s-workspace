"""Turtle Project."""

__author__ = "730431261"

from turtle import Turtle, colormode, done 


def main() -> None:
	"""The entrypoint of my scene."""
	colormode(255)
	tara: Turtle = Turtle()
	tyler: Turtle = Turtle()
	thea: Turtle = Turtle()
	tiago: Turtle = Turtle()
	draw_moon(tara, -5, 5, 100)
	draw_planet(tyler, -200, 100, 60, "blue")
	draw_planet(thea, 200, -100, 40, "green")
	for item in range(5):
		draw_large_star(tiago, -200 + item * 80, -200 + item * 40, 20)
	for item in range(8):
		draw_small_star(tiago, 100 + item * 50, 200 + item * 30, 10)
	done()


def draw_moon(turtle: Turtle, x: float, y: float, radius: float) -> None:
	"""Draw a crescent moon."""
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.fillcolor("gray")
	turtle.circle(radius)
	turtle.end_fill()
	turtle.penup()
	turtle.goto(x + radius / 2, y + radius / 2)
	turtle.pendown()
	turtle.begin_fill()
	turtle.fillcolor("black")
	turtle.circle(radius / 2)
	turtle.end_fill()
	turtle.penup()


def draw_large_star(turtle: Turtle, x: float, y: float, size: float) -> None:
	"""Draw a large star."""
	turtle.penup()
	turtle.goto(x, y) 
	turtle.pendown()
	turtle.fillcolor("yellow")
	turtle.begin_fill()
	for _ in range(5):
		turtle.forward(size)
		turtle.right(144)
	turtle.end_fill()
	turtle.penup()


def draw_small_star(turtle: Turtle, x: float, y: float, size: float) -> None:
	"""Draw a small star."""
	turtle.penup()
	turtle.goto(x, y) 
	turtle.pendown()
	turtle.fillcolor("yellow")
	turtle.begin_fill()
	for _ in range(5):
		turtle.forward(size * 0.5)
		turtle.right(144)
	turtle.end_fill()
	turtle.penup()


def draw_planet(turtle: Turtle, x: float, y: float, size: float, color: str) -> None:
	"""Draw a planet."""
	turtle.penup()
	turtle.goto(x, y) 
	turtle.pendown()
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(size)
	turtle.end_fill()
	turtle.penup()


if __name__ == "__main__":
	main()
"""Turtle Project: Uses random module in draw_meteor function and has five components (large stars, small stars, meteor, planets, and moon)."""

__author__ = "730431261"

from turtle import Turtle, colormode, done 
import random


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    tara: Turtle = Turtle()
    tyler: Turtle = Turtle()
    thea: Turtle = Turtle()
    tiago: Turtle = Turtle()
    tamara: Turtle = Turtle()
    draw_moon(tara, -5, 5, 100)
    draw_planet(tyler, -200, 100, 60, "blue")
    draw_planet(thea, 200, -100, 40, "green")
    for item in range(5):
        draw_large_star(tiago, -200 + item * 80, -200 + item * 40, 20)
    for item in range(8):
        draw_small_star(tiago, 100 + item * 50, 200 + item * 30, 10)
    draw_meteor(tamara, -300, 300, 100, 5)
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


def draw_meteor(turtle: Turtle, x: float, y: float, size: float, fragments: int) -> None:
    """Draw a meteor."""
    if size < 5 or fragments <= 0:
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    new_size = size * random.uniform(0.5, 0.8)
    new_x = x + random.uniform(-size / 2, size / 2)
    new_y = y - size * 0.6
    draw_meteor(turtle, new_x, new_y, new_size, fragments - 1)


if __name__ == "__main__":
    main()
"""EX02 - One Shot Battleship."""

__author__ = "730431261"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row = int(input("Guess a row: "))
while guess_row < 1 or guess_row > grid_size:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_column = int(input("Guess a column: "))
while guess_column < 1 or guess_column > grid_size:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

boxes: str = ""
row: int = 1

while row <= grid_size:
    column: int = 1
    row_string: str = ""
    while column <= grid_size:
        if row == guess_row and column == guess_column:
            if guess_row == secret_row and guess_column == secret_column:
                row_string += RED_BOX
            else:
                row_string += WHITE_BOX
        else:
            row_string += BLUE_BOX
        column += 1
    boxes += row_string + "\n"
    row += 1

if guess_row == secret_row and guess_column == secret_column:
    print(boxes + "Hit!")
elif guess_row == secret_row and guess_column != secret_column:
    print(boxes + "Close! Correct row, wrong column.")
elif guess_row != secret_row and guess_column == secret_column:
    print(boxes + "Close! Correct column, wrong row.")
else: 
    print(boxes + "Miss!")
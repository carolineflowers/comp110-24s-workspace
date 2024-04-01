"""EX02 - One Shot Battleship."""

__author_: "730431261"

guess_player1_row: int = int(input("Guess a row: "))
grid_size: int = 4
guess_row_0: int = int(guess_player1_row)
secret_row: int = 3
secret_column: int = 2


while guess_row_0 < 1 or guess_row_0 > 4:
    print(int(input(f"The grid is only {grid_size} by {grid_size}. Try again: ")))

guess_player1_column: int = int(input("Guess a column: "))
guess_column_0: int = int(guess_player1_column)
while guess_column_0 < 1 or guess_column_0 > 4:
    print(int(input(f"The grid is only {grid_size} by {grid_size}. Try again: ")))
        

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

hit_boxes:  str = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
blue_boxes: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
white_boxes_1: str = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
white_boxes_2: str = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX
white_boxes_3: str = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX
white_boxes_4: str = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX


while guess_row_0 == secret_row:
    if guess_column_0 == secret_column:
        print(str(blue_boxes))
        print(str(hit_boxes))
        print(str(blue_boxes))
        print(str(blue_boxes))
        print("Hit!")
        exit()
    elif guess_column_0 == 1:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_1))
        print (str(blue_boxes))
        print("Close! Correct row, wrong column.")
        exit()
    elif guess_column_0 == 3:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_3))
        print (str(blue_boxes))
        print("Close! Correct row, wrong column.")
        exit()
    elif guess_column_0 == 4:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_4))
        print (str(blue_boxes))
        print("Close! Correct row, wrong column.")
        exit()

while guess_column_0 == secret_column:
    if guess_row_0 == 1:
        print (str(white_boxes_2))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Close! Correct column, wrong row.")
        exit()
    elif guess_row_0 == 2:
        print (str(blue_boxes))
        print (str(white_boxes_2))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Close! Correct column, wrong row.")
        exit()
    elif guess_row_0 == 4:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_2))
        print("Close! Correct column, wrong row.")
        exit()

while guess_row_0 == 1:
    if guess_column_0 == 1:
        print (str(white_boxes_1))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()
    elif guess_column_0 == 3:
        print (str(white_boxes_3))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()
    elif guess_column_0 == 4:
        print (str(white_boxes_4))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()

while guess_row_0 == 2:
    if guess_column_0 == 1:
        print (str(blue_boxes))
        print (str(white_boxes_1))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()
    elif guess_column_0 == 3:
        print (str(blue_boxes))
        print (str(white_boxes_3))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()
    elif guess_column_0 == 4:
        print (str(blue_boxes))
        print (str(white_boxes_4))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print("Miss!")
        exit()

while guess_row_0 == 4:
    if guess_column_0 == 1:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_1))
        print("Miss!")
        exit()
    elif guess_column_0 == 3:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_3))
        print("Miss!")
        exit()
    elif guess_column_0 == 4:
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(blue_boxes))
        print (str(white_boxes_4))
        print("Miss!")
        exit()
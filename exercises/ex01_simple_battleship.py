"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730431261"

guess_player1: int = int(input("Pick a secret boat location between 1 and 4:"))
guess_integer_0: int = int(guess_player1)
if guess_integer_0 < 1:
    print("Error! " +str(guess_integer_0) + " too low!")
    exit()
if guess_integer_0 > 4:
    print("Error! " + str(guess_integer_0) + " too high!")
    exit()

guess_player2: str = (input("Guess a number between 1 and 4: "))
guess_integer_1: int = int(guess_player2)
if guess_integer_1 < 1:
    print("Error! " + str(guess_integer_1) + " too low!")
    exit()
if guess_integer_1 > 4:
    print("Error!" + str(guess_integer_1) + " too high!")
    exit()

if guess_integer_1 == guess_integer_0:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if guess_integer_1 == guess_integer_0 and guess_integer_0 == 1:
    print(str(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX))
if guess_integer_1 == guess_integer_0 and guess_integer_0 == 2:
    print(str(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX))
if guess_integer_1 == guess_integer_0 and guess_integer_0 == 3:
    print(str(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX))
if guess_integer_1 == guess_integer_0 and guess_integer_0 == 4:
    print(str(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX))

if guess_integer_1 == 1 and guess_integer_0 != 1:
    print(str(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX))
if guess_integer_1 == 2 and guess_integer_0 != 2:
    print(str(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX))
if guess_integer_1 == 3 and guess_integer_0 != 3:
    print(str(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX))
if guess_integer_1 == 4 and guess_integer_0 != 4:
    print(str(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX))
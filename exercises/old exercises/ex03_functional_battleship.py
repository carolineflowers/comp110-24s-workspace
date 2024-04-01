"""EX03 - Functional Battleship."""

__author__ = "730431261"
import random

size: int = 4


def input_guess(size: int, row_or_column: str) -> int:
    """Input guess function."""
    assert row_or_column == "row" or row_or_column == "column"
    guess = int(input(f"Guess a {row_or_column}: "))
    while guess < 1 or guess > size:
        guess = int(input(f"The grid is only {size} by {size}. Try again: "))
    return guess
    

def print_grid(size: int, row_guess: int, column_guess: int, user_correct: bool) -> None:
    """Print grid function."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    grid = [[BLUE_BOX] * size for int in range(size)]

    if user_correct:
        grid[row_guess - 1][column_guess - 1] = RED_BOX
    else:
        grid[row_guess - 1][column_guess - 1] = WHITE_BOX
    
    row = 0
    while row < size:
        box = 0
        while box < size:
            print(grid[row][box], end="")
            box += 1
        print()
        row += 1
        # remember () or "" represents a blank, which means return is still none and no extra boxes print bc of empty str
        # remember in code we start at, not 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Correct guess function."""
    return secret_row == guess_row and secret_column == guess_column


def main(size: int, secret_row: int, secret_column: int) -> None:
    """Main function."""
    total_turns = 5
    turn = 1

    while turn in range(1, total_turns + 1):
        # works better with for loop but technically i dont think weve covered that yet
        print(f"\n=== Turn {turn}/{total_turns} ===")
        guess_row = input_guess(size, "row")
        guess_column = input_guess(size, "column")
        player_correct = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(size, guess_row, guess_column, player_correct)

        if player_correct:
            print("Hit!\nYou won in {}/5 turns!".format(turn))
            break
            # don't even know how turn worked here totally a last min guess -- look back at notes to understand
        else:
            print(f"Miss!\nX/{total_turns} - Better luck next time!")
            breakpoint

        turn += 1

    else:
        print(f"\nX/{total_turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
# TicTacToe Game

Welcome to the TicTacToe game! This is a simple implementation of the classic TicTacToe game in Python. The game allows two players to play against each other on a 3x3 board.

## Features

- Randomly selects the first player.
- Players take turns to mark a spot on the board.
- Checks for a win condition after each move.
- Detects a draw if the board is filled without any player winning.
- Easy-to-understand text-based interface.

## How to Play

1. The game starts by randomly selecting the first player, either 'X' or 'O'.
2. Players are prompted to enter the row and column numbers to place their mark.
3. The game checks if the current player has won after each move.
4. If the board is completely filled and no player has won, the game ends in a draw.
5. The game continues until a player wins or the board is filled.

## Code Overview

The main components of the code are:

### `TicTacToe` Class

- `__init__`: Initializes an empty board.
- `create_board`: Creates a 3x3 board filled with '-' to represent empty spots.
- `get_random_first_player`: Randomly selects the first player.
- `fix_spot`: Marks a spot on the board for the current player.
- `has_player_won`: Checks if the current player has won the game.
- `is_board_filled`: Checks if the board is completely filled.
- `swap_player_turn`: Switches the turn between players.
- `show_board`: Displays the current state of the board.
- `start`: Manages the game flow, including player turns and checking win/draw conditions.


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks for playing! Enjoy your game of TicTacToe!



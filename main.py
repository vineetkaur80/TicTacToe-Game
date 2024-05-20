import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        # Check rows
        for row in self.board:
            if all(spot == player for spot in row):
                return True
        # Check columns
        for col in range(n):
            if all(self.board[row][col] == player for row in range(n)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(n)):
            return True
        if all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'Player {player} turn')
                row, col = map(int, input('Enter row & column numbers to fix spot (1-3 each): ').split())
                if self.board[row - 1][col - 1] != '-':
                    raise ValueError('This spot is already taken. Try a different spot.')
                self.fix_spot(row - 1, col - 1, player)
                game_over = self.has_player_won(player)
                if game_over:
                    self.show_board()
                    print(f'Player {player} wins the game!')
                    continue
                game_over = self.is_board_filled()
                if game_over:
                    self.show_board()
                    print('Match Draw!')
                    continue
                player = self.swap_player_turn(player)
            except (ValueError, IndexError) as err:
                print(err)
                print('Invalid input. Please enter row and column numbers between 1 and 3.')

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

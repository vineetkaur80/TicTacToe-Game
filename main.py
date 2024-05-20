import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X' if random.randint(0, 1) == 1 else 'O'
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        self.update_status()

    def on_button_click(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.has_player_won(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_filled():
                messagebox.showinfo("Tic Tac Toe", "Match Draw!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.update_status()
        else:
            messagebox.showwarning("Tic Tac Toe", "This spot is already taken. Try a different spot.")

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

    def reset_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='-')
        self.current_player = 'X' if random.randint(0, 1) == 1 else 'O'
        self.update_status()

    def update_status(self):
        self.root.title(f"Tic Tac Toe - Player {self.current_player}'s turn")

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

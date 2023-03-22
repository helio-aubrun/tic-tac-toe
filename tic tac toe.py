# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:07:43 2023

@author: aubru
"""

import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    master, text="", width=4, height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.status_label = tk.Label(master, text="Player X's turn")
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.grid(row=4, column=1)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win():
                self.status_label.config(text="Player {} wins!".format(self.current_player))
                self.disable_buttons()
            elif self.check_tie():
                self.status_label.config(text="Tie game!")
                self.disable_buttons()
            else:
                self.switch_players()
                self.status_label.config(text="Player {}'s turn".format(self.current_player))

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def switch_players(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.buttons[i][j].config(state=tk.NORMAL)
        self.status_label.config(text="Player X's turn")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

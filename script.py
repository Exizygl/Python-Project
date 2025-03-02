import os
from tkinter import *
os.system("clear")

interface = Tk()
interface.title("Tic Tac Toe")
interface.geometry("300x300")
interface.resizable(width=False, height=False)
interface.configure(bg="black")


def drawGrid(grid, rows, cols, cell_size):
    # Draw horizontal lines
    for row in range(1, rows):  # +1 to draw the bottom edge
        grid.create_line(0, row * cell_size, cols * cell_size, row * cell_size, width=5, fill="white")

    # Draw vertical lines
    for col in range(1, cols):  # +1 to draw the right edge
        grid.create_line(col * cell_size, 0, col * cell_size, rows * cell_size, width=5, fill="white")

rows = 3
cols = 3
cell_size = 100 

grid = Canvas(interface, width=cols * cell_size, height=rows * cell_size, bg="black", bd=0, highlightthickness=0)
grid.pack()

drawGrid(grid, rows, cols, cell_size)

class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(" %s | %s | %s "%(self.cells[0],self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[3],self.cells[4], self.cells[5]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[6],self.cells[7], self.cells[8]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for combo in [[0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6]]:
            if self.cells[combo[0]] == player and self.cells[combo[1]] == player and self.cells[combo[2]] == player:
                return True
        return False
    
    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return

    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def ai_move(self):
        #center move
        if self.cells[4] == " ":
            self.update_cell(4, "O")
            return
        #can win
        for combo in [[0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6]]:
            if self.cells[combo[0]] == "O" and self.cells[combo[1]] == "O" and self.cells[combo[2]] == " ":
                self.update_cell(combo[2], "O")
                return
            elif self.cells[combo[0]] == "O" and self.cells[combo[1]] == " " and self.cells[combo[2]] == "O":
                self.update_cell(combo[1], "O")
                return
            elif self.cells[combo[0]] == " " and self.cells[combo[1]] == "O" and self.cells[combo[2]] == "O":
                self.update_cell(combo[0], "O")
                return
        #block
        for combo in [[0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6]]:
            if self.cells[combo[0]] == "X" and self.cells[combo[1]] == "X" and self.cells[combo[2]] == " ":
                self.update_cell(combo[2], "O")
                return
            elif self.cells[combo[0]] == "X" and self.cells[combo[1]] == " " and self.cells[combo[2]] == "X":
                self.update_cell(combo[1], "O")
                return
            elif self.cells[combo[0]] == " " and self.cells[combo[1]] == "X" and self.cells[combo[2]] == "X":
                self.update_cell(combo[0], "O")
                return
        #random move
        import random
        while True:
            rand = random.randint(0,8)
            if self.cells[rand] == " ":
                self.update_cell(rand, "O")
                return

board = Board()

# interface call

interface.mainloop()




""" def print_header():
    print("Tic Tac Toe\n")

def refresh_screen():
    # clear the screen
    os.system("clear")

    # print the header
    print_header()

    # show the board
    board.display()
 
while True:
     refresh_screen()

    # get X input
    x_choice = int(input("\nX) Please choose 1-9. > "))
    
    # update cell   
    board.update_cell(x_choice - 1, "X")

    refresh_screen()

    # check for X win
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again.lower() != "y":
            break
        else:
            board.reset()
            continue

    # check for tie
    if board.is_tie():
        print("\nTie game!\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again.lower() != "y":
            break
        else:
            board.reset()
            continue

    

    # get O input
    
    board.ai_move()
    
    refresh_screen()

    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again.lower() != "y":
            break
        else:
            board.reset()
            continue    

    if board.is_tie():
        print("\nTie game!\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again.lower() != "y":
            break
        else:
            board.reset()

    

     """

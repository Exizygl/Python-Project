import os
os.system("clear")

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

board = Board()



def print_header():
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
    o_choice = int(input("\nO) Please choose 1-9. > "))

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

    # update cell
    board.update_cell(o_choice - 1, "O")

    
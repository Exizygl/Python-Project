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

    # get O input
    o_choice = int(input("\nO) Please choose 1-9. > "))

    # update cell
    board.update_cell(o_choice - 1, "O")
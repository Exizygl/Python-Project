import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(" %s | %s | %s "%(self.cells[0],self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[0],self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[0],self.cells[1], self.cells[2]))


board = Board()
board.display()
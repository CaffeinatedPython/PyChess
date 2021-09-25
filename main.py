#8x8 board
# - black/white squares
#define pieces as objects
#draw board to console
#King = K
#Queen = Q = 9 pawns
#Knight = N = 3 pawns
#Bishop = B = 3 pawns
#Rook = R = 5 pawns
#pawn =

import PySimpleGUI as sg

class Square:
    def __init__(self, color, piece, occupied, name):
        self.color = color
        self.piece = piece
        self.occupied = occupied #BOOL
        self.name = name

    def __repr__(self):
        return("%s(color: %s, piece: %s, occupied: %s)" % (self.name, self.color, self.piece, str(self.occupied)))

class GameBoard:
    def __init__(self):
        board = []


def create_board():
    board = []
    for index in range(8):
        row = []
        for each in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            color = "white"
            if index % 2 == 0 and each in ['b', 'd', 'f', 'h']:
                color = 'black'
            elif index % 2 == 1 and each in['a', 'c', 'e', 'g']:
                color = 'black'
            row.append(sg.Button(button_color=color, size=(4,4), pad = (0,0), border_width=1, key=(index,each)))
        board.append(row)

    return(board)






    print(board)
def create_window():

    layout = create_board()

    layout += [[sg.Cancel()]]

   # window = sg.Window('PyChess', layout)
    return(layout)


def main():

    window = sg.Window('PyChess',create_window())
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
    window.close()

if __name__ == "__main__":
    main()







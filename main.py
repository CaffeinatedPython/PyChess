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
import base64
from PIL import Image, ImageTk

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
            color = "blue"
            if (index % 2 == 0 and each in ['a', 'c', 'e', 'g']) or (index % 2 == 1 and each in ['b', 'd', 'f', 'h']):
                color = 'grey'
            keyName = (each + str(index))
            #row.append(sg.Button(button_text=keyName, button_color=color, size=(2,2),
            #                     pad = (0,0), border_width=1, key=keyName, use_ttk_buttons=True))
            #                    #use_ttk_buttons was causing issues on Mac for mouse over
            row.append(sg.Image(key=keyName, tooltip=keyName, background_color=color, size=(90,90), pad = (1,1),
                                expand_x=True, expand_y=True, enable_events=True))
        board.insert(0,row)  #Needs insert instead of append otherwise backward

    return(board)



def create_window():

    layout = create_board()

    layout += [[sg.Cancel(),sg.Button("New Game")]]

   # window = sg.Window('PyChess', layout)
    return(layout)


def main():

    window = sg.Window('PyChess',create_window())

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == "New Game":
            new_game(window)
            window['e0'].update(filename='images/kingb.png', size=(90,90))


    window.close()

if __name__ == "__main__":
    main()







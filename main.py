#8x8 board
# - black/white squares
#define pieces as objects
#draw board to console




class Square:
    def __init__(self, color, piece, occupied, name):
        self.color = color
        self.piece = piece
        self.occupied = occupied #BOOL
        self.name = name

class GameBoard:
    def __init__(self):
        board = []


def create_board():
    board = []
    for index in range(8):
        for each in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            color = "white"
            if each in ["a", "c", "e", "g"] and index % 2 != 0:
                color = "black"
            piece = ""
            occupied = False
            name = each + str(index)
            board.append(Square(color, piece, occupied, name))

    print(board)

def main():
    create_board()

if __name__ == "__main__":
    main()







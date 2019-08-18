class Board(object):
    """A class that creates a board or move map to store Knight position for a Knight's Tour""" 
    def __init__(self, size):
        self.size = size
        self.board = [([0] * size) for row in range(size)]

    def is_empty(self, x, y):
        """Is the tile empty? Checks if the specified (x,y) position is empty, i.e. is 0."""
        return self.board[x][y] == 0

    def place_knight(self, move_number, x, y):
        """Log the Knight's move number in the specified position."""
        self.board[x][y] = move_number

    def print_board(self):
        """Prints the Knight's Tour of the board as a move map, '1' being the knight's starting location."""
        for i in range(self.size):
            for j in range(self.size):
                print(str(self.board[i][j]).rjust(2) + " ", end="")
            print()

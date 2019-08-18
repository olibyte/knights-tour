class Knight(object):
    """A class defining a Knight object to carry out a Knight's Tour."""
    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1

    def move(self, x, y):
        """Move the Knight object to a new position."""
        self.x = x
        self.y = y

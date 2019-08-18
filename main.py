"""PBL Task 2: Knight's Tour
    Python Implementation that generates the solution as a move map to the console.
    
    note that this is an OPEN tour (i.e. the knight does not have to end its tour on the square from which it started,
    though there are versions available.

    This program was developed and guided by the following solutions:
    http://blog.justsophie.com/algorithm-for-knights-tour-in-python/
    Pynaconda's (Sophie Li's) Solution to the existing problem on HackerRank (python)

    https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/
    Geek for Geek's C++ Implementation
    """
#  Libraries
from knight import Knight
from board import Board

#  Constants
# Define the dimensions of the board. This determines the maximum number of moves. O(n^2)
BOARD_SIZE = 8
MAX_MOVES = BOARD_SIZE**2

# These two sets determine the combinations of possible moves for the Knight.
#i.e. Offsets for the Knight's current position.
MOVE_X = [-2, -1, 1, 2, 2, 1, -1, -2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]

#  Functions

def main():
    """Executes the main application."""
    # Instantiate the x & y co-ordinates. Note that 9 and 9 are 'off the board' and therefore invalid.
    x = 9
    y = 9

    # Take x & y User input. For error tolerance, Loop until we receive a valid input (i.e. cannot start the Knight 'off' the board).
    while (x < 1 or x > BOARD_SIZE) or (y < 1 or y > BOARD_SIZE):
        x, y = input("Enter the Knight's starting position as X & Y co-ordinates (1-" + str(BOARD_SIZE)
                     + ") separated by a space (e.g. 4 4): ").split()
        x, y = [int(x), int(y)]

        if x < 1 or x > BOARD_SIZE:
            print("ERROR::Invalid input: x must be 1-" + str(BOARD_SIZE))

        if y < 1 or y > BOARD_SIZE:
            print("ERROR::Invalid input: y must be 1-" + str(BOARD_SIZE))

    print()

    # Create a Knight object at the given X,Y input.
    knight = Knight(x, y)

    # Instantiate the board. The Knight's initial position (input) is given with move 1.
    board = Board(BOARD_SIZE)
    board.place_knight(1, knight.x, knight.y)

    #  Test for all valid possible moves and special cases.
    for current_move in range(2, MAX_MOVES + 1):
        num_possibilities, next_x, next_y = get_num_possibilities(knight, board)
        min_exits_idx = 0 #index of minimum number of exits

        # If there are no possibilities left, then end the tour prematurely. Special case that doesn't come up often.
        if num_possibilities == 0:
            print("The knight's tour ended prematurely at (" + str(knight.x + 1)
                  + "," + str(knight.y + 1) + ") during move #"
                  + str(current_move - 1) + ".")
            print()
            break
        
        # If there's more than 1 move possible, find next tile with the
        # fewest number of exits. This is the core of Warndorff's Rule.
        elif num_possibilities > 1:
            exits = find_min_exits(board, num_possibilities, next_x, next_y)
            min_exits_idx = get_idx_smallest_num_exits(num_possibilities, exits)

        # Move the knight, marking its location on the board.     
        knight.move(next_x[min_exits_idx], next_y[min_exits_idx])
        board.place_knight(current_move, knight.x, knight.y)

    # Print the board to the console. The board is represented as a move map.
    board.print_board()

def get_num_possibilities(knight, board):
    """Tests each move ahead of position (i,j) then
    list the possibilities for the next move (next_i(l), next_j(l))."""
    num_possibilities = 0
    next_x = [0] * BOARD_SIZE
    next_y = [0] * BOARD_SIZE

    # Test all possible moves.
    for i in range(0, BOARD_SIZE):
        # Check the next move for validity without storing it by using a temp.
        temp_x = knight.x + MOVE_X[i]
        temp_y = knight.y + MOVE_Y[i]

        #if the move is valid and the tile is available, increment the number of possible moves.
        if (temp_x >= 0 and temp_x < BOARD_SIZE
            and temp_y >= 0 and temp_y < BOARD_SIZE
            and board.is_empty(temp_x, temp_y)):
            next_x[num_possibilities] = temp_x
            next_y[num_possibilities] = temp_y
            num_possibilities = num_possibilities + 1

    # Return the number of possibilities and list of next positions.
    return num_possibilities, next_x, next_y

def find_min_exits(board, num_possibilities, next_x, next_y):
    """Find the next valid move with the minimum number of exits.
    (In other words, explore first the move with the fewest number of next moves
    Note: The term 'exits' is used here, but is commonly referred to as 'paths' in graph-theory literature."""
    # Store the number of exits for each move.
    exits = [0] * BOARD_SIZE

    # Check all the exits for each possible move.    
    for i in range(0, num_possibilities):
        num_exits = 0

        #  Nested loop checking the number of exits of the move after each next move.
        # Sounds complicated, but all we're doing is for each move we check, we're checking one more move ahead for validity
        # until we reach a dead-end.
        for j in range(0, 8):
            check_x = next_x[i] + MOVE_X[j]
            check_y = next_y[i] + MOVE_Y[j]

            # If the exit of the move after the next move is valid, then
            # increment the number of possible exits.
            if (check_x >= 0 and check_x < BOARD_SIZE
                and check_y >= 0 and check_y < BOARD_SIZE
                and board.is_empty(check_x, check_y)):
                num_exits = num_exits + 1

        # Store the number of exits.
        exits[i] = num_exits

    # Return the number of exits for each move.
    return exits

def get_idx_smallest_num_exits(num_possibilities, exits):
    """Find the smallest number of exits. The Knight searches for the move that will yield the fewest number of exits 
     (Warnsdorff's Rule)."""
    min_exits_idx = 0
    current_num_exit = exits[0]

    # Uses a for loop to iterate through the number of possible moves, finding the index containing the smallest number of exits.
    for i in range(1, num_possibilities):
        if current_num_exit > exits[i]:
            current_num_exit = exits[i]
            min_exits_idx = i

    # Return the index of the smallest number of exits.
    return min_exits_idx

#  Execute main
main()
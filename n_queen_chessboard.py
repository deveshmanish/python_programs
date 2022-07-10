def initialize(board, n):
    for key in ['queen', 'row', 'column', 'nwse', 'swne']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['column'][i] = 0
    for i in range(-(n - 1), n):
        board['nwse'][i] = 0
    for i in range(2 * n - 1):
        board['swne'][i] = 0


def checkSquare(i, j, board):
    return board['queen'][i] == -1 and board['row'][i] == 0 and board['column'][j] == 0 and board['nwse'][
        j - i] == 0 and board['swne'][i + j] == 0


def addQueen(i, j, board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['column'][j] = 1
    board['nwse'][j - i] = 1
    board['swne'][i + j] = 1


def removeQueen(i, j, board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['column'][j] = 0
    board['nwse'][j - i] = 0
    board['swne'][i + j] = 0


def placeQueen(row, board):
    n = len(board['queen'].keys())
    for column in range(n):
        if checkSquare(row, column, board):
            addQueen(row, column, board)
            if row == n - 1:
                return True
            else:
                extendSolution = placeQueen(row + 1, board)
            if extendSolution:
                return True
            else:
                removeQueen(row, column, board)
    else:
        return False


board = {}
n = int(input('How many queens?'))
initialize(board, n)
if placeQueen(0, board):
    print(board)

'''
Q3) Tic-Tac-Toe Board Printer 
Print a 3x3 Tic-Tac-Toe board with numbers or player symbols. 
'''
def print_board_with_symbols(board):
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-" * 9)
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]

print_board_with_symbols(board)

def print_board(board):
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['bot_L'] + '|' + board['bot_M'] + '|' + board['bot_R'])
board = {'top_L': ' ','top_M': ' ','top_R': ' '
       ,'mid_L': ' ','mid_M': ' ','mid_R': ' '
       ,'bot_L': ' ','bot_M': ' ','bot_R': ' '}
print_board(board)
turn = 'X'
for pos in range(len(board)):
    print('Which move will you take?')
    move = input()
    board[move] = turn
    print_board(board)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

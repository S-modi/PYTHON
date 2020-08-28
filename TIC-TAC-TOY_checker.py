def is_solved(board):
    if board[0][0]==board[1][1]==board[2][2]==1 or board[0][2]==board[1][1]==board[2][0]==1 or board[0][0]==board[0][1]==board[0][2]==1 or board[1][0]==board[1][1]==board[1][2]==1  or board[2][0]==board[2][1]==board[2][2]==1 or board[0][0]==board[1][0]==board[2][0]==1 or board[0][1]==board[1][1]==board[2][1]==1 or board[0][2]==board[1][2]==board[2][2]==1:
        return '1 is win'
    elif board[0][0]==board[1][1]==board[2][2]==2 or board[0][2]==board[1][1]==board[2][0]==2 or board[0][0]==board[0][1]==board[0][2]==2 or board[1][0]==board[1][1]==board[1][2]==2  or board[2][0]==board[2][1]==board[2][2]==2 or board[0][0]==board[1][0]==board[2][0]==2 or board[0][1]==board[1][1]==board[2][1]==2 or board[0][2]==board[1][2]==board[2][2]==2:
        return '2 is win'
    elif board[0][0]==0 or board[0][1]==0 or board[0][2]==0 or  board[1][0]==0 or board[1][1]==0 or board[1][2]==0 or  board[2][0]==0 or board[2][1]==0 or board[2][2]==0:
        return 'moves is left'
    else:
        return 'Match draw'
   

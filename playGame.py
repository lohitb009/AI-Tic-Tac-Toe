'''
Count are:     60694 -- Minimax Algo
Count are:     3383  -- Alpha Beta Pruning
Count are:   2466  -- Alpha Beta Pruning
'''
from board import TicTacToe

class playGame:
    
    '''
    player O move is minimizing-move
    player X move is maximizing-move
    '''
    def __init__(self):
        # create an obj of class TicTacToe game
        self.ticTacToe = TicTacToe()
        self.ticTacToe.printBoard()
        
        self.__alpha = float('-inf')
        self.__beta = float('+inf')
        self.count = 0
        
    # get the player move
    def playerMove(self):
        position = int(input("Enter the position of 'O' player:\t"))
        self.ticTacToe.insertLetter('O', position)
    
    # get the bot move
    def botMove(self):
        # maximizing move
        maximizingScore = float('-inf')
        bestScore = 0
        
        # initialize position
        position = None
        
        # iterate the dictionary
        for key in self.ticTacToe.board:
            
            if self.ticTacToe.board[key] == ' ':
                
                # action-- available-space for bot
                self.ticTacToe.board[key] = 'X'
                # recurse-- perform miniMax --- player O move
                result = self.miniMaxAlphaBeta(0,False,self.__alpha,self.__beta)
                # bestScore
                bestScore = result[0]
                # alpha
                if self.__alpha < result[1]:
                    self.__alpha = result[1]
                # backtrack-- undo the previous move
                self.ticTacToe.board[key] = ' '
                # update the maximizing move
                if maximizingScore < bestScore:
                    maximizingScore = bestScore
                    position = key                
                '''alpha beta pruning case'''
                # chk for prunning condition -- base condition
                # chk for alpha-beta pruning
                if self.__alpha < maximizingScore:
                    self.__alpha = maximizingScore
                if self.__alpha >= self.__beta: 
                    # no need to chk further --- just break from the iteration
                    break
                '''alpha beta pruning case'''
                
        '''end of for loop'''
        self.ticTacToe.insertLetter('X', position)
        
    """
    def botMove(self):
        # maximizing move
        maximizingScore = float('-inf')
        bestScore = 0
        
        # initialize position
        position = None
        
        # iterate the dictionary
        for key in self.ticTacToe.board:
            
            if self.ticTacToe.board[key] == ' ':
                
                # action-- available-space for bot
                self.ticTacToe.board[key] = 'X'
                # recurse-- perform miniMax --- player O move
                bestScore = self.miniMax(0,False)
                # backtrack-- undo the previous move
                self.ticTacToe.board[key] = ' '
                # update the maximizing move
                if maximizingScore < bestScore:
                    maximizingScore = bestScore
                    position = key
        '''end of for loop'''
        self.ticTacToe.insertLetter('X', position)
    
    # initialize minimax function
    """
    """
    def miniMax(self,lvl,maximizingMove):
        self.count += 1
        
        # base-case
        if self.ticTacToe.chkWinner('X'):
            # bot won
            return 1
        elif self.ticTacToe.chkWinner('O'):
            # player won
            return -1
        elif self.ticTacToe.checkDraw():
            # its a draw
            return 0
        
        # logic-case
        if maximizingMove:
            # bot move
            maximizingScore = float('-inf')
            bestScore = 0
            
            # iterate the dictionary
            for key in self.ticTacToe.board:
                
                if self.ticTacToe.board[key] == ' ':        
                    # action-- available-space for bot
                    self.ticTacToe.board[key] = 'X'
                    # recurse-- perform miniMax --- player O move
                    bestScore = self.miniMax(lvl+1,False)
                    # backtrack-- undo the previous move
                    self.ticTacToe.board[key] = ' '
                    # update the maximizing move
                    maximizingScore = max(maximizingScore,bestScore)
            '''end of for loop iteration'''
            return maximizingScore
            
        else:
            # player move
            minimizingScore = float('inf')
            bestScore = 0
            
            # iterate the dictionary
            for key in self.ticTacToe.board:
                
                if self.ticTacToe.board[key] == ' ':        
                    # action-- available-space for bot
                    self.ticTacToe.board[key] = 'O'
                    # recurse-- perform miniMax --- player X move
                    bestScore = self.miniMax(lvl+1,True)
                    # backtrack-- undo the previous move
                    self.ticTacToe.board[key] = ' '
                    # update the maximizing move
                    minimizingScore = min(minimizingScore,bestScore)
            '''end of for loop iteration'''
            return minimizingScore
    """
    
    # inititalize minimax alpha beta pruning
    def miniMaxAlphaBeta(self,lvl,maximizingMove,alpha,beta):
        
        # base-case
        if self.ticTacToe.chkWinner('X'):
            # bot won
            return (1,alpha,beta)
        elif self.ticTacToe.chkWinner('O'):
            # player won
            return (-1,alpha,beta)
        elif self.ticTacToe.checkDraw():
            # its a draw
            return (0,alpha,beta)
        
        # logic-case
        if maximizingMove:
            # bot move
            maximizingScore = float('-inf')
            bestScore = 0
            
            # iterate the dictionary
            for key in self.ticTacToe.board:
                
                if self.ticTacToe.board[key] == ' ':        
                    # action-- available-space for bot
                    self.ticTacToe.board[key] = 'X'
                    # recurse-- perform miniMax --- player O move
                    result = self.miniMaxAlphaBeta(lvl+1,False,alpha,beta)
                    # bestScore
                    bestScore = result[0]
                    # alpha
                    if alpha < result[1]:
                        alpha = result[1]
                    # backtrack-- undo the previous move
                    self.ticTacToe.board[key] = ' '
                    
                    # update the maximizing move
                    maximizingScore = max(maximizingScore,bestScore)
                    '''alpha beta pruning case'''
                    # chk for alpha-beta pruning
                    # chk for prunning condition -- base condition
                    if alpha < maximizingScore:
                        alpha = maximizingScore
                    if alpha >= beta:
                        # no need to chk further --- just return from the iteration
                        break
                    '''alpha beta pruning case'''
                    
            '''end of for loop iteration'''
            return (maximizingScore,alpha,beta)
            
        else:
            # player move
            minimizingScore = float('inf')
            bestScore = 0
            
            # iterate the dictionary
            for key in self.ticTacToe.board:
                
                if self.ticTacToe.board[key] == ' ':        
                    # action-- available-space for bot
                    self.ticTacToe.board[key] = 'O'
                    # recurse-- perform miniMax --- player X move
                    result = self.miniMaxAlphaBeta(lvl+1,True,alpha,beta)
                    # bestScore
                    bestScore = result[0]
                    # beta
                    if beta > result[2]:
                        beta = result[2]
                    # backtrack-- undo the previous move
                    self.ticTacToe.board[key] = ' '
                    # update the maximizing move
                    minimizingScore = min(minimizingScore,bestScore)
                    '''alpha beta pruning case'''
                    # chk for prunning condition -- base condition
                    # chk for alpha-beta pruning
                    if beta > minimizingScore:
                        beta = minimizingScore
                    if alpha >= beta:
                        # no need to chk further --- just return from the iteration
                        break
                    '''alpha beta pruning case'''
            '''end of for loop iteration'''
            return (minimizingScore,alpha,beta)
    
play = playGame()
# assume 3*3 board
movesCount = 0

while True:
    
    # player move
    play.playerMove()
    if play.ticTacToe.chkWinner('O'):
        print("O is the winner i.e. player")
        break
    movesCount+= 1
    
    '''
    # bot move 
    play.botMove()
    if play.ticTacToe.chkWinner('X'):
        print("X is the winner i.e. bot")
        break
    movesCount += 1
    '''
    
    # print("Moves Count is:\t",movesCount)
    # base-case: chk for moves
    if movesCount == (play.ticTacToe.dimension)*(play.ticTacToe.dimension):
        print("Tie Game")
        break
    
    # bot move 
    play.botMove()
    if play.ticTacToe.chkWinner('X'):
        print("X is the winner i.e. bot")
        break
    movesCount += 1
    
    '''
    # player move
    play.playerMove()
    if play.ticTacToe.chkWinner('O'):
        print("O is the winner i.e. player")
        break
    movesCount+= 1
    '''
        
    # base-case: chk for moves
    if movesCount == (play.ticTacToe.dimension)*(play.ticTacToe.dimension):
        print("Tie Game")
        break
'''end of while loop'''

print("Count are:\t",play.count)
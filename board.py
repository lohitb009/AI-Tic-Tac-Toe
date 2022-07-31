'''
Created on 18-Jul-2022

@author: lohit
'''
class TicTacToe():
    def __init__(self,n=3):
        self.board = self.makeBoard(n)
        self.dimension = n
        
    # initialize board
    def makeBoard(self,n):
        # n*n game
        totalCount = n*n
        count = 1
        boardDict = {}
        while count <= totalCount:
            if count not in boardDict:
                boardDict[count] = ' '
                count += 1
        '''end of while loop'''
        return boardDict
    
    # print the board
    def printBoard(self):
        count = 1
        toPrint = ''
        print('START')
        while count != len(self.board)+1:
            toPrint += '|'+ str(self.board[count]) +'|\t'
            if (count % self.dimension) == 0:
                print(toPrint)
                toPrint = ''
            count += 1
        '''end of while loop'''
        print('END')
    # chk if space is free
    def spaceIsFree(self,position):
        if self.board[position] == ' ':
            return True
        return False
    
    # chk for draw
    def checkDraw(self):
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True
    
    # chk for row
    def chkRow(self,letter):
        startIdx = 1
        valIdx = startIdx
        
        # assum win is False
        win = False
        
        # initialize row 
        row = 1
        while startIdx < self.dimension*self.dimension:
            
            if valIdx <= self.dimension*row and self.board[valIdx] == letter:
                
                if valIdx%self.dimension*row == 0:
                    # I have a match in my current-row
                    win = True
                    break
                # update the valIdx
                valIdx += 1
            else:
                # I dont have match in current-row
                startIdx += self.dimension
                valIdx = startIdx
                row += 1
                
        return win
        
    # chk for col
    def chkCol(self,letter):
        # initialize start and count index
        startIdx = 1 
        
        # initialize valIdx
        valIdx = startIdx
        count = 0 # to count in a col
        
        # assume win is False
        win = False
        
        while startIdx <= self.dimension:
            
            # base-case
            if count == self.dimension:
                win = True
                break
            
            # logic-case
            if self.board[valIdx] == letter:
                # update the valIdx
                valIdx += self.dimension
                # update the count
                count += 1
            
            else:
                startIdx += 1
                valIdx = startIdx 
                count = 0
                
        '''end of while loop'''
        return win
    
    # chk for backwardDiagonal
    def chkBackwardDiagonal(self,letter):
        startIdx = 1
        
        # assume win is True
        win = True
        
        while startIdx <= self.dimension*self.dimension:
            if self.board[startIdx] == letter:
                startIdx += (self.dimension+1)
            else:
                win = False
                break
        '''end of while loop'''
        
        return win            
    
    # chk for backwardDiagonal
    def chkForwardDiagonal(self,letter):
        startIdx = self.dimension
        
        # assume win is True
        win = True
        
        while startIdx < self.dimension*self.dimension:
            if self.board[startIdx] == letter:
                startIdx += (self.dimension-1)
            else:
                win = False
                break
        '''end of while loop'''
        
        return win           
    
    def chkWinner(self,letter):
        # chk row
        # chk col
        # chk backward
        # chk forward
        if self.chkRow(letter) or self.chkCol(letter) or self.chkBackwardDiagonal(letter) or self.chkForwardDiagonal(letter):
            # if either of my case is True
            return True
        else:
            return False
     
    # make the move and chk for the win
    def insertLetter(self,letter,position):
        # make any move within n*n
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard()
            # chk the conditions
            
            # case-1 chk for draw
            if self.checkDraw():
                print("Its TIE")
                return
            
            # case-2 chk for win in row
            elif self.chkRow(letter):
                if letter == 'X':
                    print("Bot wins!")
                    return
                else:
                    print("Player wins!")
                    return
            
            # case-3 chk for win in col
            elif self.chkCol(letter):
                if letter == 'X':
                    print("Bot wins!")
                    return
                else:
                    print("Player wins!")
                    return
            
            # case-4 chk for backward diagonal
            elif self.chkBackwardDiagonal(letter):
                if letter == 'X':
                    print("Bot wins!")
                    return
                else:
                    print("Player wins!")
                    return
            
            # case-5 chk for foward diagonal
            elif self.chkForwardDiagonal(letter):
                if letter == 'X':
                    print("Bot wins!")
                    return
                else:
                    print("Player wins!")
                    return


# ticTacToe = TicTacToe()
# print(ticTacToe.board)
# ticTacToe.board[3]= 'X'
# ticTacToe.board[6]= 'X'
# ticTacToe.printBoard()
# ticTacToe.insertLetter('X',9)

from random import randint

class ttt:

    def __init__(self):
        self.T = [0,0,0,0,0,0,0,0,0]

    def convBoardStateToStr(self, x, pos):
       if x==1:
          return "X"
       elif x==2:
          return "O"
       else:
          return str(pos)

    def printBoard(self):
       if len(self.T) != 9:
          return False
       for i in range(0,len(self.T)):
          if self.T[i] != 0 and self.T[i] != 1 and self.T[i] != 2:
             return False
       # note: to put a multi-line python statement you can use
       #       a "\" to make things look easier to read
       str = " " + \
        self.convBoardStateToStr(self.T[0],0) + "|"+ self.convBoardStateToStr(self.T[1],1) + "|"+ self.convBoardStateToStr(self.T[2],2)
       print str
       print "---|---|---"
       str = " " + \
        self.convBoardStateToStr(self.T[3],3) + "|"+ self.convBoardStateToStr(self.T[4],4) + "|"+ self.convBoardStateToStr(self.T[5],5)
       print str
       print "---|---|---"
       str = " " + \
        self.convBoardStateToStr(self.T[6],6) + "|"+ self.convBoardStateToStr(self.T[7],7) + "|"+ self.convBoardStateToStr(self.T[8],8)
       print str
       return True

    def analyzeBoard(self):
        if self.T[0] == self.T[1] == self.T[2] != 0:
            return self.T[0]
        if self.T[3] == self.T[4] == self.T[5] != 0:
            return self.T[3]
        if self.T[6] == self.T[7] == self.T[8] != 0:
            return self.T[6]
        if self.T[0] == self.T[3] == self.T[6] != 0:
            return self.T[0]
        if self.T[1] == self.T[4] == self.T[7] != 0:
            return self.T[1]
        if self.T[2] == self.T[5] == self.T[8] != 0:
            return self.T[2]
        if self.T[0] == self.T[4] == self.T[8] != 0:
            return self.T[0]
        if self.T[2] == self.T[4] == self.T[6] != 0:
            return self.T[2]
        # n_opens=reduce(lambda x,y:x+y,map(lambda x:1 if x==0 else 0,t))
        n_opens = 0
        for i in range(0, len(self.T), 1):
            if self.T[i] == 0:
                n_opens = n_opens + 1

        if n_opens == 0:
            return 3
        else:
            return 0

    def genRandomMove(self, player):
        n_opens = 0
        for i in range(0, len(self.T), 1):
            if self.T[i] == 0:
                n_opens = n_opens + 1
        if n_opens == 0:
            return -1
        else:
            while True:
                move = randint(0, 8)
                if self.T[move] == 0:
                    return move

    def genWinningMove(self, player):
        for i in range(0, len(self.T), 1):
            if self.T[i] == 0:
                self.T[i] = player
                if self.analyzeBoard() == player:
                    return i
                self.T[i] = 0
        return -1

    def genNonLoser(self, player):
        if player == 1:
            opponent = 2
        else:
            opponent = 1
        return self.genWinningMove(opponent)

    def Move(self, x, player):
        if self.T[x] == 0:
            self.T[x] = player
            return True
        else:
            return False

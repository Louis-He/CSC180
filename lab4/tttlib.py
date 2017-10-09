from random import randint

class ttt:

    def convBoardStateToStr(self, x, pos):
       if x==1:
          return "X"
       elif x==2:
          return "O"
       else:
          return str(pos)

    def printBoard(self,T):
       if len(T) != 9:
          return False
       for i in range(0,len(T)):
          if T[i] != 0 and T[i] != 1 and T[i] != 2:
             return False
       # note: to put a multi-line python statement you can use
       #       a "\" to make things look easier to read
       str = " " + \
        self.convBoardStateToStr(T[0],0) + "|"+ self.convBoardStateToStr(T[1],1) + "|"+ self.convBoardStateToStr(T[2],2)
       print str
       print "---|---|---"
       str = " " + \
        self.convBoardStateToStr(T[3],3) + "|"+ self.convBoardStateToStr(T[4],4) + "|"+ self.convBoardStateToStr(T[5],5)
       print str
       print "---|---|---"
       str = " " + \
        self.convBoardStateToStr(T[6],6) + "|"+ self.convBoardStateToStr(T[7],7) + "|"+ self.convBoardStateToStr(T[8],8)
       print str
       return True

    def analyzeBoard(self, t):
        if t[0] == t[1] == t[2] != 0:
            return t[0]
        if t[3] == t[4] == t[5] != 0:
            return t[3]
        if t[6] == t[7] == t[8] != 0:
            return t[6]
        if t[0] == t[3] == t[6] != 0:
            return t[0]
        if t[1] == t[4] == t[7] != 0:
            return t[1]
        if t[2] == t[5] == t[8] != 0:
            return t[2]
        if t[0] == t[4] == t[8] != 0:
            return t[0]
        if t[2] == t[4] == t[6] != 0:
            return t[2]
        # n_opens=reduce(lambda x,y:x+y,map(lambda x:1 if x==0 else 0,t))
        n_opens = 0
        for i in range(0, len(t), 1):
            if t[i] == 0:
                n_opens = n_opens + 1

        if n_opens == 0:
            return 3
        else:
            return 0

    def genRandomMove(self, u, player):
        n_opens = 0
        for i in range(0, len(u), 1):
            if u[i] == 0:
                n_opens = n_opens + 1
        if n_opens == 0:
            return -1
        else:
            while True:
                move = randint(0, 8)
                if u[move] == 0:
                    return move

    def genWinningMove(self, t, player):
        u = list(t)
        for i in range(0, len(u), 1):
            if u[i] == 0:
                u[i] = player
                if self.analyzeBoard(u) == player:
                    return i
                u[i] = 0
        return -1

    def genNonLoser(self, t, player):
        if player == 1:
            opponent = 2
        else:
            opponent = 1
        return self.genWinningMove(t, opponent)

    #def Move(self, x, player):

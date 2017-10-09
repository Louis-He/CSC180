import random
def genBoard():
    T=[0,0,0,0,0,0,0,0,0]
    return T


def printBoard(T):
    if len(T) != 9:
        return False
    accum = []
    for i in range(0, len(T), 1):
        if T[i] == 0:
            accum = accum + [str(i)]
        elif T[i] == 1:
            accum = accum + ['X']
        elif T[i] == 2:
            accum = accum + ['O']
        else:
            return False
        return True

def analyzeBoard(T):
    if len(T)!=9:
        return -1
    for i in range(0,len(T),1):
        if T[i] !=0 and T[i] !=1 and T[i] !=2:
            return -1
            break
    if(T[0]== T[1]== T[2]==1 or T[3]== T[4]== T[5]==1 or T[6]== T[7]== T[8]==1 or T[0]== T[4]== T[8]==1 or T[2]== T[4]== T[6]==1 or T[0]== T[3]== T[6]==1 or        T[1]== T[4]== T[7]==1 or T[2] ==T[5]== T[8]==1):
        return 1
    if(T[0]== T[1]== T[2]==2 or T[3]== T[4]== T[5]==2 or T[6]== T[7]== T[8]==2 or T[0]== T[4]== T[8]==2 or T[2]== T[4]== T[6]==2 or T[0]== T[3]== T[6]==2 or        T[1]== T[4]== T[7]==2 or T[2] ==T[5]== T[8]==2):
        return 2
    for i in range (0,len(T),1):
         if T[i]==0:
            return 0
    else:
        return 3

def genRandomMove (T,player):
    if len(T)!=9:
        return -1
    for i in T:
        if i > 2 or i < 0:
            return -1
    x = 0
    while True:
        x += 1
        u = random.randint(0, 8)
        if T[u] == 0:
            return u
        if x >= 50:
            return -1

def genWinningMove(T, player):
    if len(T) != 9:
        return -1
    '''
    for i in T:
        if i > 2 or i < 0:
            return -1
    '''
    x = 0
    for i in range(0, 9):
        if T[i] == 1 or T[i] == 2:
            x = x + 1
    if x == 1:
        return -1
    if T[0] == T[1] == player and T[2] == 0:
        return 2
    if T[0] == T[2] == player and T[1] == 0:
        return 1
    if T[2] == T[1] == player and T[0] == 0:
        return 0
    if T[3] == T[4] == player and T[5] == 0:
        return 5
    if T[3] == T[5] == player and T[4] == 0:
        return 4
    if T[4] == T[5] == player and T[3] == 0:
        return 3
    if T[6] == T[7] == player and T[8] == 0:
        return 8
    if T[8] == T[6] == player and T[7] == 0:
        return 7
    if T[7] == T[8] == player and T[6] == 0:
        return 6
    if T[0] == T[3] == player and T[6] == 0:
        return 6
    if T[0] == T[6] == player and T[3] == 0:
        return 3
    if T[3] == T[6] == player and T[0] == 0:
        return 0
    if T[4] == T[1] == player and T[7] == 0:
        return 7
    if T[7] == T[1] == player and T[4] == 0:
        return 4
    if T[7] == T[4] == player and T[1] == 0:
        return 1
    if T[2] == T[5] == player and T[8] == 0:
        return 8
    if T[2] == T[8] == player and T[5] == 0:
        return 5
    if T[5] == T[8] == player and T[2] == 0:
        return 2
    if T[0] == T[4] == player and T[8] == 0:
        return 8
    if T[0] == T[8] == player and T[4] == 0:
        return 4
    if T[8] == T[4] == player and T[0] == 0:
        return 0
    if T[2] == T[4] == player and T[6] == 0:
        return 6
    if T[2] == T[6] == player and T[4] == 0:
        return 4
    if T[4] == T[6] == player and T[2] == 0:
        return 2

    def genNonLoser(T, player):
        if player == 2:
            player = 1
        else:
            player = 2
        if len(T) != 9:
            return -1
        '''
        for i in T:
            if i > 2 or i < 0:
                return -1
        '''
        x = 0
        for i in range(0, len(T), 1):
            if T[i] == 1 or T[i] == 2:
                x = x + 1
        if x == 1:
            return -1
        if T[0] == T[1] == player and T[2] == 0:
            return 2
        if T[0] == T[2] == player and T[1] == 0:
            return 1
        if T[2] == T[1] == player and T[0] == 0:
            return 0
        if T[3] == T[4] == player and T[5] == 0:
            return 5
        if T[3] == T[5] == player and T[4] == 0:
            return 4
        if T[4] == T[5] == player and T[3] == 0:
            return 3
        if T[6] == T[7] == player and T[8] == 0:
            return 8
        if T[8] == T[6] == player and T[7] == 0:
            return 7
        if T[7] == T[8] == player and T[6] == 0:
            return 6
        if T[0] == T[3] == player and T[6] == 0:
            return 6
        if T[0] == T[6] == player and T[3] == 0:
            return 3
        if T[3] == T[6] == player and T[0] == 0:
            return 0
        if T[4] == T[1] == player and T[7] == 0:
            return 7
        if T[7] == T[1] == player and T[4] == 0:
            return 4
        if T[7] == T[4] == player and T[1] == 0:
            return 1
        if T[2] == T[5] == player and T[8] == 0:
            return 8
        if T[2] == T[8] == player and T[5] == 0:
            return 5
        if T[5] == T[8] == player and T[2] == 0:
            return 2
        if T[0] == T[4] == player and T[8] == 0:
            return 8
        if T[0] == T[8] == player and T[4] == 0:
            return 4
        if T[8] == T[4] == player and T[0] == 0:
            return 0
        if T[2] == T[4] == player and T[6] == 0:
            return 6
        if T[2] == T[6] == player and T[4] == 0:
            return 4
        if T[4] == T[6] == player and T[2] == 0:
            return 2

        '''
        T = [0,0,0,0,0,0,0,0,0]
        print(analyzeBoard(T))
        print (genRandomMove(T,1))
        '''
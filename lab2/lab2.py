import random
def genBoard():
  T=[0,0,0,0,0,0,0,0,0]
  return T

def analyzeBoard(T):
  for i in range(0,7,3):
    if T[0+i]==T[1+i]==T[2+i]==2:
      return 2
  for i in range(0,7,3):
    if T[0+i]==T[1+i]==T[2+i]==1:
      return 1
  for i in range(0,3):
    if T[0+i]==T[3+i]==T[6+i]==2:
      return 2
  for i in range(0,3):
    if T[0+i]==T[3+i]==T[6+i]==1:
      return 1
  if T[0]==T[4]==T[8]==2 or T[2]==T[4]==T[6]==2:
    return 2
  if T[0]==T[4]==T[8]==1 or T[2]==T[4]==T[6]==1:
    return 1
  if T[0]!=0 and T[1]!=0 and T[2]!=0 and T[3]!=0 and T[4]!=0 and \
                  T[5]!=0 and T[6]!=0 and T[7]!=0 and T[8]!=0:
    return 3
  else:
    return 0


def genRandomMove(T,player):
    if analyzeBoard(T) != 0 or player != 1 and player != 2:
        return -1
    import random
    while True:
        x = random.randint(0,8)
        if T[x] == 0:
            return x

def genWinningMove(T,player):
   if analyzeBoard(T) != 0 or player != 1 and player != 2:
       return -1
   if T[0]==T[1]==player and T[2]==0:
       return 2
   elif T[1]==T[2]==player and T[0]==0:
       return 0
   elif T[0]==T[2]==player and T[1]==0:
       return 1
   elif T[3]==T[4]==player and T[5]==0:
       return 5
   elif T[4]==T[5]==player and T[3]==0:
       return 3
   elif T[3]==T[5]==player and T[4]==0:
       return 4
   elif T[6]==T[7]==player and T[8]==0:
       return 8
   elif T[7]==T[8]==player and T[6]==0:
       return 6
   elif T[6]==T[8]==player and T[7]==0:
       return 7
   elif T[0]==T[3]==player and T[6]==0:
       return 6
   elif T[1]==T[4]==player and T[7]==0:
       return 7
   elif T[2]==T[5]==player and T[8]==0:
       return 8
   elif T[0]==T[6]==player and T[3]==0:
       return 3
   elif T[1]==T[7]==player and T[4]==0:
       return 4
   elif T[2]==T[8]==player and T[5]==0:
       return 5
   elif T[3]==T[6]==player and T[0]==0:
       return 0
   elif T[4]==T[7]==player and T[1]==0:
       return 1
   elif T[5]==T[8]==player and T[2]==0:
       return 2
   elif T[0]==T[4]==player and T[8]==0:
       return 8
   elif T[0]==T[8]==player and T[4]==0:
       return 4
   elif T[4]==T[8]==player and T[0]==0:
       return 0
   elif T[2]==T[4]==player and T[6]==0:
       return 6
   elif T[2]==T[6]==player and T[4]==0:
       return 4
   elif T[4]==T[6]==player and T[2]==0:
       return 2
   else:
       return -1

def genNonLoser(T,player):
    if analyzeBoard(T) != 0 or player != 1 and player != 2:
        return -1
    if T[0] == T[1] ==abs(3-player) and T[2]==0:
        return 2
    elif T[1] == T[2] ==abs(3-player) and T[0]==0:
        return 0
    elif T[0] == T[2] ==abs(3-player) and T[1]==0:
        return 1
    elif T[3] == T[4] ==abs(3-player) and T[5]==0:
        return 5
    elif T[4] == T[5] ==abs(3-player) and T[3]==0:
        return 3
    elif T[3] == T[5] ==abs(3-player) and T[4]==0:
        return 4
    elif T[6] == T[7] ==abs(3-player) and T[8]==0:
        return 8
    elif T[7] == T[8] ==abs(3-player) and T[6]==0:
        return 6
    elif T[6] == T[8] ==abs(3-player) and T[7]==0:
        return 7
    elif T[0] == T[3] ==abs(3-player) and T[6]==0:
        return 6
    elif T[1] == T[4] ==abs(3-player) and T[7]==0:
        return 7
    elif T[2] == T[5] ==abs(3-player) and T[8]==0:
        return 8
    elif T[0] == T[6] ==abs(3-player) and T[3]==0:
        return 3
    elif T[1] == T[7] ==abs(3-player) and T[4]==0:
        return 4
    elif T[2] == T[8] ==abs(3-player) and T[5]==0:
        return 5
    elif T[3] == T[6] ==abs(3-player) and T[0]==0:
        return 0
    elif T[4] == T[7] ==abs(3-player) and T[1]==0:
        return 1
    elif T[5] == T[8] ==abs(3-player) and T[2]==0:
        return 2
    elif T[0] == T[4] ==abs(3-player) and T[8]==0:
        return 8
    elif T[0] == T[8] ==abs(3-player) and T[4]==0:
        return 4
    elif T[4] == T[8] ==abs(3-player) and T[0]==0:
        return 0
    elif T[2] == T[4] ==abs(3-player) and T[6]==0:
        return 6
    elif T[2] == T[6] ==abs(3-player) and T[4]==0:
        return 4
    elif T[4] == T[6] ==abs(3-player) and T[2]==0:
        return 2
    else:
        return -1

def printBoard(T):
    print"",
    for i in range(0,9):
        if T[i]<>0 and T[i]<>1 and T[i]<>2:
            return False
        if i==3 or i==6:
            print ""
            print "---|---|---"
            print "",
        if T[i]==0:
            print i,
            if i==8:
                print "",
        if T[i]==1:
            print "X",
        if T[i]==2:
            print "O",
        if i==0 or i==1 or i==3 or i==4 or i==6 or i==7:
            print"|",
    if len(T)<>9:
        return False
    print ""
    return True

T=[0,2,2,0,0,0,0,0,0]
print genNonLoser(T,1)
#print analyzeBoard(T)

import sys


FIN=""
FOUT=""
COL=""
DIR=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      print "INFO: processing",arg
      if arg == "--fin":
         if i != nargs-1:
            FIN=sys.argv[i+1]
            skip=True
      elif arg == "--fout":
         if i != nargs-1:
            FOUT=sys.argv[i+1]
            skip=True
      elif arg == "--col":
         if i != nargs-1:
            COL=sys.argv[i+1]
            skip=True
      elif arg == "--dir":
         if i != nargs-1:
            DIR=sys.argv[i+1]
            skip=True
      else:
         print "ERR: unknown arg:",arg
   else:
      skip=False

print "INFO: FIN", FIN
print "INFO: FOUT", FOUT
print "INFO: COL",COL
print "INFO: DIR",DIR

if DIR == '+':
    up = True
else:
    up = False


def genSortKey(col,up):
    def key(x):
        return x[int(col)] if up else -x[int(col)]
    return key
sortKey = genSortKey(COL, up)

#INPUT
try:
    f = open(FIN, 'r')
    lines = f.readlines()
    f.close()
except:
    print 'ERR: file DO NOT EXIST.'

#PROCESS
accum = []
for i in lines:
    j = i.split('\n')[0]
    k=j.split(',')
    r=[]
    for x in k:
        r = r +[int(x)]
    accum = accum + [r]

result = sorted(accum, key=sortKey)

#OUTPUT
try:
    g = open(FOUT, 'w')
    for i in range(len(result)):
        for j in range(len(result[0])):
            if j != len(result[0]) - 1:
                g.write(str(result[i][j])+',')
            else:
                g.write(str(result[i][j])+'\n')
except:
    print 'ERR: cannot write to file "dataout"'




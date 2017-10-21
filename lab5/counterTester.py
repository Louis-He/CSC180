from counterlib import *
result1 = 5050
result2 = 2550

# test the addition from 1 to 100
test1 = counter(0)
for i in range (1,101):
    test1.evolve(i)
if test1.getstate() == result1:
    print 'test1: ' + str(test1.getstate()) + ', TEST PASSED.'
else:
    print 'test1: ' + str(test1.getstate()) + ', TEST FAILED.'

# test the addition of even number from 2 to 100
test2 = counter(0)
for i in range (1,51):
    test2.evolve(i * 2)
if test2.getstate() == result2:
    print 'test2: ' + str(test2.getstate()) + ', TEST PASSED.'
else:
    print 'test2: ' + str(test2.getstate()) + ', TEST FAILED.'
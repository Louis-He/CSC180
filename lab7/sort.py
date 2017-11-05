# D.1. python CODE
def bubbleSort(array):
    n = len(array)
    swapped = True
    status = True
    try:
        while swapped == True:
            swapped = False
            for i in range(1, n):
                if array[i - 1] > array[i]:
                    #swap(array[i-1], array[i])
                    tmp = array[i - 1]
                    array[i - 1] = array[i]
                    array[i] = tmp
                    swapped = True
    except:
        status = False
    return (status, array)

'''
#TESTING CODE FOR 'BubbleSort'
a = [4,2,3,8,7,12,1,-1]
print bubbleSort(a)
'''

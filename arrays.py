import numpy

def arrays(arr):
    arr = list(map(float, arr))
    arr.reverse()
    arr = numpy.array(arr, float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

import numpy
numpy.set_printoptions(legacy = "1.13")
l = list(map(int, input().split()))
print(numpy.eye(l[0], l[1], k = 0))

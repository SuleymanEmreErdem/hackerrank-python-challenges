import numpy
N = int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))
A, B = numpy.array(A), numpy.array(B)
print(numpy.matmul(A, B))

from itertools import product
A = input().split()
A = list(map(int, A))
B = input().split()
B = list(map(int, B))
pro = tuple(product(A, B))
for item in pro:
    print(item, end=" ")

from itertools import product
def square(x):
    return x*x
res = 0
K, M = input().split()
arr = []
for _ in range(int(K)):
    arr.append(list(map(int, input().split()))[1:])
combination = [p for p in product(*arr)]
for item in combination:
    mapped_item = list(map(square, item))
    val = sum(mapped_item) % int(M) 
    if val > res:
        res = val
    else:
        pass
print(res)

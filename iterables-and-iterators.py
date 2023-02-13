N = int(input())
letters = input().split()
K = int(input())
from itertools import combinations
comb = list(combinations(letters, K))
num = 0
denom = 0
for item1 in comb:
    for item2 in item1:
        if item2 == "a":
            num += 1
            break
    denom += 1    
print(num/denom)

from itertools import combinations
S, k = input().split()
S = sorted([*S])
for a in range(1, int(k)+1):    
    per = list(combinations(S, a))
    for item in per:
        for i in range(0, a):
            print(item[i], end="")
        print(" ")

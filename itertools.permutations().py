from itertools import permutations
S, k = input().split()
S = sorted([*S])
per = list(permutations(S, int(k)))
for item in per:
    for i in range(0, int(k)):
        print(item[i], end="")
    print(" ")

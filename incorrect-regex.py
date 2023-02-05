import re
T = int(input())
S = []
for i in range(T):
    S.append(input())
for item in S:
    try:
        re.compile(item)
        print(True)
    except re.error:
        print(False)
        

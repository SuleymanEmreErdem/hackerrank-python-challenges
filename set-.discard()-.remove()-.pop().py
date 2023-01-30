n = int(input())
s = set(map(int, input().split()))
N = int(input())
comm = []
for _ in range(N):
    comm.append(input().split())
for i in range(N):
    if comm[i][0] == "remove":
        s.remove(int(comm[i][1]))
    elif comm[i][0] == "discard":
        s.discard(int(comm[i][1]))
    elif comm[i][0] == "pop":
        s.pop()
print(sum(s))

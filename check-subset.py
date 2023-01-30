T = int(input())
for _ in range(T):
    A_num = int(input())
    A = set(map(int, input().split()))
    B_num = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))

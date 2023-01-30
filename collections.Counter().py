from collections import Counter
sum_ = 0
X = int(input())
shoe_list = input().split()
shoe_list = list(map(int, shoe_list))
shoe_list = Counter(shoe_list)
N = int(input())
size_price = [None] * N
for i in range(0, N):
    size_price[i] = list(map(int, input().split()))
for a in range(0, N):
    if shoe_list[size_price[a][0]] == 0 or None:
        pass
    else:
        sum_ += size_price[a][1]
        shoe_list[size_price[a][0]] -= 1
print(sum_)

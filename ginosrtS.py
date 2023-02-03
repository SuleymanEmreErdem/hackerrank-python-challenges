S = list(input())
upper, lower, odd, even = [], [], [], []
for item in S:
    if item.isupper():
        upper.append(item)
    elif item.islower():
        lower.append(item)
    elif item.isdigit():
        if int(item)%2 == 0:
            even.append(item)
        else:
            odd.append(item)
upper.sort(), lower.sort(), odd.sort(), even.sort()
print("".join(lower)+"".join(upper)+"".join(odd)+"".join(even))

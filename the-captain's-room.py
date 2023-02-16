K = int(input())
numbers = list(map(int, input().split()))
groups = {}
for number in numbers:
    if number in groups:
        groups[number].append(number)
    else:
        groups[number] = [number]
for i, group in enumerate(groups.values()):
    if len(group) == 1:
        print(group[0])
        break

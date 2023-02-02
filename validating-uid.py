T = int(input())
arr1 = []
arr2 = []
for _ in range(T):
    arr1.append(input())
for item in arr1:
    numbers = sum(c.isdigit() for c in set(item))
    letters = sum(c.isalpha() for c in set(item))
    if item.isalnum() and len(item) == 10 and numbers >= 3 and letters >= 2 and len(set(item)) == len(item):
        print("Valid")
    else:
        print("Invalid")

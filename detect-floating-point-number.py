T = int(input())
arr = []
for _ in range(T):
    arr.append(input())
for item in arr:
    try:
        b = float(item)
        if str(int(b)) == str(b) or not "." in item:
            raise
        print(True)
    except:
        print(False)

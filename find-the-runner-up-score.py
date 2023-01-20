if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    a = list(map(int, arr))
    
    a.sort()
    a.reverse()
    b = a[0]
    for c in range(n):
        if a[c]<b:
            break
    print(a[c])

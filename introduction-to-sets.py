def average(array):
    res = sum(set(array))/len(set(array))
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

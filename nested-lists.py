def sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

if __name__ == '__main__':
    N = int(input())
    arr = []
    res = []
    for _ in range(N):
        stu = [input(), float(input())]
        arr.append(stu)
    arr = sort(arr)
    low = arr[0][1]
    for i in range(len(arr)):
        if arr[i][1] > low:
            res.append(arr[i][0])
            try:    
                if arr[i+1][1] == arr[i][1]:
                    res.append(arr[i+1][0])
                break
            except:
                break
    res.sort()
    for item in res:
        print(item)

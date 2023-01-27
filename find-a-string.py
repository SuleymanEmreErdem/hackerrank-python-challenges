def count_substring(string, sub_string):
    sum = 0
    for i in range(0, len(string)):
        if sub_string == string[i:len(sub_string)+i]:
            sum+=1
    return sum

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

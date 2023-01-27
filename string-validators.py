def counter(s):
    stat = False
    for i in range(0, len(s)):
        if s[i].isalnum() == True:
            stat = True
            print(stat)
            break
    if stat == False:
        print(stat)
    stat = False
    for i in range(0, len(s)):
        if s[i].isalpha() == True:
            stat = True
            print(stat)
            break
    if stat == False:
        print(stat)
    stat = False    
    for i in range(0, len(s)):
        if s[i].isdigit() == True:
            stat = True
            print(stat)
            break
    if stat == False:
        print(stat)
    stat = False    
    for i in range(0, len(s)):
        if s[i].islower() == True:
            stat = True
            print(stat)
            break
    if stat == False:
        print(stat)
    stat = False    
    for i in range(0, len(s)):
        if s[i].isupper() == True:
            stat = True
            print(stat)
            break
    if stat == False:
        print(stat)
    stat = False    
if __name__ == '__main__':
    s = input()
    counter(s)

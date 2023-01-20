if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list = []
    a=x
    b=y
    c=z
    
    while a>=0:
        while b>=0:
            while c>=0:
                if (a+b+c)!=n:
                    list.append([a,b,c])
                c-=1
            b-=1
            c=z
        a-=1
        b=y
        
    list.reverse()
    print(list)

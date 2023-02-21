def count_digits(s):
    digit = 0
    for let in s:
        if let.isdigit():
            digit += 1
    return digit

def count_group(st):
    if st.split() == st.split("-"):
        stat = True
    else:
        st = st.split("-")
        stat = True
        for group in st:
            if len(group) == 4:
                stat = True
            else:
                stat = False
                break
    return stat

def repeat(s):    
    from itertools import groupby
    s = list(s)
    for item in s:
        if item == "-":
            s.remove(item)
    groups = groupby(s)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    stat = True
    for i in range(len(result)):
        if result[i][1] >= 4:
            stat = False
            break
    return stat
        
def digit_hyphen(s):
    stat = True
    for num in s:
        if num.isdigit() or num == "-":
            stat = True
        else:
            stat = False
            break
    return stat           
        
N = int(input())
cards = []
for _ in range(N):
    cards.append(input())
for card in cards:
    if (count_digits(card) == 16) and (card[0] == "4" or card[0] == "5" or card[0] == "6") and repeat(card) and count_group(card) and digit_hyphen(card):
        print("Valid")
    else:
        print("Invalid")

def solve(s):
    s = list(s)
    s[0] = s[0].upper()
    for i in range(len(s)):
        if s[i] != " ":
            pass
        else:
            s[i+1] = s[i+1].upper()
    return "".join(s)

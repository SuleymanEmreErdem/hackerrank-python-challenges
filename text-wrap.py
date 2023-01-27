import textwrap

def wrap(string, max_width):
    i = (len(string))%max_width
    for _ in range(0, int(len(string)/max_width)):
        string = string[max_width:] + "\n" + string[:max_width]
    string = string[i:] + "\n" + string[:i]
    string = string.strip()
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

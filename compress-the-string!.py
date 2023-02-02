from itertools import groupby

def generate_output(input_str):
    groups = [(len(list(group)), int(char)) for char, group in groupby(input_str)]
    return ' '.join(f'({count}, {digit})' for count, digit in groups)

input_str = input()
print(generate_output(input_str))

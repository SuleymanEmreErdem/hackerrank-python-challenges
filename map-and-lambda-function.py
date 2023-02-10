cube = lambda x: x**3

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return sequence
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

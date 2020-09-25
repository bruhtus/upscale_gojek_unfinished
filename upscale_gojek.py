from fire import Fire

def main(a, b, string):
    h(pow(a, b), string)

def g(string):
    i = 0
    new_str = ''
    while i < (len(string) - 1):
        new_str = new_str + string[i + 1]
        i = i + 1

    #print(f'another: {new_str}')
    return new_str

def f(string):
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string
    else:
        return (f(g(string)) + string[0])

def h(n, string):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1

        string = f(string)
        print(string)

    return string

def pow(x, y):
    if y == 0:
        return 1
    else:
        return (x * pow(x, y-1))

if __name__ == '__main__':
    Fire(main)

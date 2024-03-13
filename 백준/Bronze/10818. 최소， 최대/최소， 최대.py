import os


def main():
    tokens = map(int, iter(os.read(0, os.stat(0).st_size).split()))
    next(tokens)
    a = 1 << 29
    b = -a
    for x in tokens:
        if x < a:
            a = x
        if x > b:
            b = x
    os.write(1, (str(a) + ' ' + str(b)).encode())
    os._exit(0)


main()
import sys

def add(a, b):
    return a - b


if __name__ == '__main__':
    a, b = map(int, sys.argv[1:])
    print(f"The sum of {a} and {b} is {add(a,b)}")

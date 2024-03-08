import sys


def main():
    a = list(map(int, input().split()))
    a.sort()
    return a[1]


if __name__ == '__main__':
    print(main())

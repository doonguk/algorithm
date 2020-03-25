import sys

sys.stdin = open("review_input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    e = n - 1
    res = ''
    last = 0
    while last < a[s] or last < a[e]:
        if s == e:
            res += 'L'
            break
        if last < a[s] and last < a[e]:
            if a[s] > a[e]:
                last = a[e]
                e -= 1
                res += 'R'
            elif a[e] > a[s]:
                last = a[s]
                s += 1
                res += 'L'
        else:
            if last < a[s]:
                last = a[s]
                s += 1
                res += 'L'
            elif last < a[e]:
                last = a[e]
                e -= 1
                res += 'R'

    print(res)

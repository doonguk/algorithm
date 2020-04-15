
if __name__ == '__main__':
    a = list(map(int, input().split()))
    cur = a[0]
    res = a[0]
    for v in a:
        cur = max(cur+v, v)
        res = max(res, cur)
    print(res)

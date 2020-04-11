if __name__ == '__main__':
    n = int(input())
    a = list()
    while n > 0:
        a.append(n % 10)
        n //= 10
    a.sort(reverse=True)

    res = 0
    for i in range(len(a)):
        res = res * 10 + a[i]
    print(res)
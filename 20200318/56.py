if __name__ == '__main__':
    n = int(input())
    cnt = 1
    while True:
        n -= cnt
        if n > cnt:
            cnt += 1
        else:
            break
    print(cnt)

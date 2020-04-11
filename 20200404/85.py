def convertPrime(origin, target, n):
    for idx, v in enumerate(origin):
        i = 0
        while v > 0:
            target[idx][n - 1 - i] = v % 2
            v //= 2
            i += 1
    return target


def solution(n, arr1, arr2):
    a1 = [[0] * n for _ in range(n)]
    a2 = [[0] * n for _ in range(n)]

    a1 = convertPrime(arr1, a1, n)
    a2 = convertPrime(arr2, a2, n)
    answer = [''] * n
    for y in range(n):
        for x in range(n):
            if a1[y][x] == 1 or a2[y][x] == 1:
                answer[y] += '#'
            else:
                answer[y] += ' '
    return answer
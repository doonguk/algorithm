def reverse(self, x: int) -> int:
    flag = False
    if x < 0:
        flag = True
        x *= -1
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x //= 10

    if flag:
        res *= -1
    if -2 ** 31 > res or res > 2 ** 31 - 1:
        return 0
    return res
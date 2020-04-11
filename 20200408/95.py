def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    else:
        a = list()
        while x > 0:
            a.append(x % 10)
            x //= 10

        for i in range(len(a) // 2):
            if a[i] != a[-1 - i]:
                return False
        return True
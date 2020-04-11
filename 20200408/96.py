def romanToInt(self, s: str) -> int:
    stack = list(str)
    res = 0
    while stack:
        s = stack.pop()
        if s == 'M':
            if stack[-1] == 'C':
                stack.pop()
                res += 900
            else:
                res += 1000
        elif s == 'D':
            if stack[-1] == 'C':
                stack.pop()
                res += 400
            else:
                res += 500
        elif s == 'C':
            if stack[-1] == 'X':
                stack.pop()
                res += 90
            else:
                res += 100
        elif s == 'L':
            if stack[-1] == 'X':
                stack.pop()
                res += 40
            else:
                res += 50
        elif s == 'X':
            if stack[-1] == 'I':
                stack.pop()
                res += 9
            else:
                res += 10
        elif s == 'V':
            if stack[-1] == 'I':
                stack.pop()
                res += 4
            else:
                res += 5
        else:
            res += 1
    return res
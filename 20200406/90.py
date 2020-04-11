def solution(s):
    stack = list()
    for v in s:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return not(stack)
import sys
sys.stdin = open("input35.txt", "rt")

expression = input()
stack = list()
for a in expression:
    if a.isdecimal():
        stack.append(int(a))
    else:
        first = stack.pop()
        second = stack.pop()
        if a == '+':
            stack.append(second + first)
        elif a == '-':
            stack.append(second - first)
        elif a == '*':
            stack.append(second * first)
        else:
            stack.append(second / first)

print(stack[0])

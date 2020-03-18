import sys
sys.stdin = open("input34.txt", "rt")

a = input()
stack = []
res = ''
for i in a:
    if i.isdecimal():
        res += i
    else:
        if i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(i)
        elif i == '(':
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)
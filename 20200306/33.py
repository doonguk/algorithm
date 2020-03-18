import sys
sys.stdin = open("input33.txt", "rt")

lasers = input()
stack = list()

res = 0
for i in range(len(lasers)):
    if lasers[i] == '(':
        stack.append(lasers[i])
    else:
        stack.pop()
        if lasers[i-1] == '(':
            res += len(stack)
        else:
            res += 1

print(res)
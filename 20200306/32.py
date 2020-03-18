import sys
sys.stdin = open("input32.txt", "rt")

n, m = map(int, input().split())
numbers = list()
while n > 0:
    numbers.insert(0, n % 10)
    n //= 10
stack = list()

for a in numbers:
    while stack and m > 0 and stack[-1] < a:
        stack.pop()
        m -= 1
    stack.append(a)

if m != 0:
    stack = stack[:-m]

print(stack)






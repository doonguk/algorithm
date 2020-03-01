import sys
sys.stdin = open("input9.txt", "rt")

n = int(input())
max = -2147000000

def calculate(args):
    a, b, c = args
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    return money

for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()
    _money = calculate(tmp)
    if _money > max:
        max = _money

print(max)

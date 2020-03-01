import sys
sys.stdin = open("input8.txt", "rt")
n = int(input())
numbers = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res*10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for a in range(2, x//2+1):
        if x % a == 0:
            return False
    else:
        return True

for a in numbers:
    rev = reverse(a)
    if isPrime(rev):
        print(rev, end=' ')

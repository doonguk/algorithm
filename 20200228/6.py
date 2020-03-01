import sys
sys.stdin = open("input6.txt", "rt")
n = int(input())
numbers = list(map(int, input().split()))
max = -2147000000
res = 0

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


for number in numbers:
    total = digit_sum(number)
    if max < total:
        max = total
        res = number

print(number)

import sys
sys.stdin = open("input41.txt", "rt")

a1 = input()
a2 = input()
def hash_func(x):
    if x.isupper():
        return ord(x)-65
    else:
        return ord(x)-97+26
h1 = list([0] * 52)
h2 = list([0] * 52)
for x in a1:
    h1[hash_func(x)] += 1
for x in a2:
    h2[hash_func(x)] += 1

for i in range(52):
    if h1[i] != h2[i]:
        print('NO')
        break
else:
    print('YES')

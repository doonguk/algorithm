import sys
sys.stdin = open("input20.txt", "rt")

def check(a):
    for y in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for x in range(9):
            ch1[a[y][x]] = 1
            ch2[a[x][y]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for y in range(3):
        for x in range(3):
            ch3 = [0]*10
            for y2 in range(3):
                for x2 in range(3):
                    ch3[a[y*3+y2][x*3+x2]] = 1
            if sum(ch3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print('YES')
else:
    print('NOT')
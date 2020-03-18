import sys
sys.stdin = open("input44.txt", "rt")

def DFS(x):
    if x == 0:
        return
    DFS(x//2)
    print(x%2, end='')


if __name__ == "__main__":
    n = int(input())
    DFS(n)
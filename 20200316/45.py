def DFS(v):
    if v > 7:
        return
    print(v, end=' ')
    DFS(2*v)
    DFS(2*v+1)


if __name__ == "__main__":
    DFS(1)


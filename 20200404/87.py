def solution(m, n, board):
    board = list(map(list, board))
    dx = [1, 1, 0]
    dy = [0, 1, 1]
    answer = 0
    cnt = 0
    while True:
        ch = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                for k in range(3):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if board[y][x] == -1 or xx >= n or yy >= m or board[y][x] != board[y + dy[k]][x + dx[k]]:
                        break
                else:
                    if ch[y][x] == 0:
                        ch[y][x] = 1
                        cnt += 1
                    for k in range(3):
                        if ch[y + dy[k]][x + dx[k]] == 0:
                            ch[y + dy[k]][x + dx[k]] = 1
                            cnt += 1
        if cnt == 0:
            break
        answer += cnt
        cnt = 0

        # delete
        for y in range(m):
            for x in range(n):
                if ch[y][x] == 1:
                    now = y  # 현재 처리 값
                    before = now - 1  # 위에 값
                    while before >= 0 and board[before][x] != -1:
                        board[now][x] = board[before][x]
                        now -= 1
                        before -= 1

                    board[now][x] = -1

    return answer
def solution(board, moves):
    stack = list()
    cnt = 0
    for v in moves:
        x = v -1
        for y in range(len(board)):
            if board[y][x] != 0:
                if stack and stack[-1] == board[y][x]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[y][x])
                board[y][x] = 0
                break
    return cnt
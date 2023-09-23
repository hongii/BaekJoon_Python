from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maxH = max(map(max, board))


def bfs(i, j, h):
    dq = deque()
    dq.append((i, j))

    while dq:
        x, y = dq.popleft()
        for a in range(4):
            x_ = x + dx[a]
            y_ = y + dy[a]
            if 0 <= x_ < n and 0 <= y_ < n and board[x_][y_] > h and not visited[x_][y_]:
                dq.append((x_, y_))
                visited[x_][y_] = True


maxCnt = 0
for h in range(maxH):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, h)
                cnt += 1
    maxCnt = max(cnt, maxCnt)
    if maxCnt == n*n:
        break
print(maxCnt)

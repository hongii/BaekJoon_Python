from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
war = []
for i in range(m):
    war.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Wpower, Bpower = 0, 0

def bfs(i, j, color):
    dq = deque()
    war[i][j] = 0
    dq.append((i, j))
    cnt = 1  
    while dq:
        i, j = dq.popleft()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < m and 0 <= y < n and war[x][y] == color:
                war[x][y] = 0
                cnt += 1
                dq.append((x, y))
    return cnt**2

for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            Wpower += bfs(i, j, "W")
        elif war[i][j] == "B":
            Bpower += bfs(i, j, "B")
print(Wpower, Bpower)
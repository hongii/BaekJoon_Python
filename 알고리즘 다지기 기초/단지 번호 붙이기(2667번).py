# 완전탐색 dfs/bfs 문제
# dfs 재귀호출 구문에서 하나의 단지가 탐색 끝나면 cnt를 반환해야 하는데(재귀호출 탈출) 재귀 탈출 부분에서 return cnt 안하고 뻘짓하느라 시간 소요
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")
n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
for i in range(n):
    tmp = list(input())
    graph.append(tmp)

def dfs(i, j, cnt):
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < n and graph[x][y] == '1':
            graph[x][y] = '0'
            cnt = dfs(x, y, cnt+1)
    return cnt

house = 0
totalCnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            house += 1
            graph[i][j] = '0'
            cnt = dfs(i, j, 1)
            totalCnt.append(cnt)
print(house)
totalCnt.sort()
for c in totalCnt:
    print(c)
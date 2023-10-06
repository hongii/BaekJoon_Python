# 위상정렬 + dp
import sys
from collections import deque
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    b, a, cnt = map(int, input().split())
    graph[a].append((b, cnt))
    indegree[b] += 1

dq = deque()
needs = [[0]*(n+1) for _ in range(n+1)]
basic = []  # 기본 부품 종류를 담는 리스트
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
        basic.append(i)

while dq:
    x = dq.popleft()

    for (y, cnt) in graph[x]:
        if x in basic:  # x번 부품이 기본 부품이라면, y부품(중간 부품)을 만들기 위한 부품의 갯수로 바로 count
            needs[y][x] += cnt
        else:  # x번 부품이 중간부품이라면, x번 부품을 만들 때 필요한 기본 부품의 갯수 * x번 부품이 필요한 갯수 만큼 count
            for i in range(1, n+1):
                needs[y][i] += needs[x][i] * cnt

        indegree[y] -= 1
        if indegree[y] == 0:
            dq.append(y)

for i in basic:
    if needs[n][i] != 0:
        print(i, needs[n][i])

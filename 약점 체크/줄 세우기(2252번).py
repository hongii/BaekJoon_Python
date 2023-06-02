# 위상정렬 문제
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0]*(n+1)
res = []
for _ in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    inDegree[u] += 1

def topological_sort():
    dq = deque()
    for i in range(1, len(inDegree)):
        if inDegree[i] == 0:
            dq.append(i)
    
    while dq:
        now = dq.popleft()
        res.append(now)
        for x in graph[now]:
            inDegree[x] -= 1
            if inDegree[x] == 0:
                dq.append(x)
topological_sort()
print(*res)
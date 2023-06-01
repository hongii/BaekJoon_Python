# 왜 시간초과 나는지 모르겠음....혹시 몰라서 다른사람 다익스트라 풀이 확인했는데 내 코드랑 똑같은데 왜 내꺼는 시간초과...?
# pypy3으로 제출하면 통과, python3로 제출하면 시간초과
import heapq
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")

def Dijkstra(start, end):
    hq = []
    distance = [10e9]*(n+1)
    distance[start] = 0
    heapq.heappush(hq, [0, start])

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue
        
        for x in cities[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(hq, [cost, x[0]])
    return distance[end]

n, m = int(input()), int(input())
cities = [[] for _ in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    cities[s].append((e, w))
start, end = map(int, input().split())
res = Dijkstra(start, end)
print(res)
# 다익스트라
# 첫번째 코드 => 도착 노드 나오면 바로 경로 구해버리기(시간 조금 더 빠름)
import sys
import heapq
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 4\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline  # 이거 안해주면 4060ms, 이거 처리해주면 216ms..... => 꼭 readline 처리 해주자

n = int(input())
m = int(input())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    cities[a].append((b, w))

start, end = map(int, input().split())


def Dikjstra(start, end):
    path = [i for i in range(n+1)]
    hq = []
    cost = [float('inf')] * (n+1)
    cost[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        c, now = heapq.heappop(hq)
        if cost[now] < c:
            continue

        if now == end:
            print(cost[end])
            res = [now]
            while now != start:
                res.append(path[now])
                now = path[now]
            print(len(res))
            print(*res[::-1])
            break

        for v, w in cities[now]:
            if c + w < cost[v]:
                cost[v] = c + w
                path[v] = now
                heapq.heappush(hq, (cost[v], v))


Dikjstra(start, end)


# 두번째 코드 => start에서 다른 모든 노드까지의 최소 비용을 구한 후, 최소비용과 경로를 출력
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 4\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
m = int(input())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    cities[a].append((b, w))

start, end = map(int, input().split())


def Dikjstra(start, end):
    path = [i for i in range(n+1)]
    hq = []
    cost = [float('inf')] * (n+1)
    cost[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        c, now = heapq.heappop(hq)
        if cost[now] < c:
            continue

        for v, w in cities[now]:
            if c + w < cost[v]:
                cost[v] = c + w
                path[v] = now
                heapq.heappush(hq, (cost[v], v))

    # 최소 비용, 경로 출력
    print(cost[end])
    res = [end]
    tmp = end
    while tmp != start:
        res.append(path[tmp])
        tmp = path[tmp]
    print(len(res))
    print(*res[::-1])


Dikjstra(start, end)

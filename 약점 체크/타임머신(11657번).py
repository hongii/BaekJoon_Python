# 벨만포드 알고리즘
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distances = [float('inf')]*(n+1)


def BellmanFord(start):
    distances[start] = 0  # 출발 노드 거리는 0

    # n-1번만큼 모든 간선을 확인하고 최단거리를 갱신
    for _ in range(n-1):
        for a, b, w in edges:
            if distances[a] != float('inf') and distances[a]+w < distances[b]:
                distances[b] = distances[a]+w

    # 음수 사이클 확인 -> 마지막 n번째 때 최단거리가 갱신되는 노드가 발생한다면, 이는 음수 사이클이 존재하는 것.
    # cf. 원래 최단거리는 최대 n-1번안에 무조건 정해지므로 n번째 때 최단거리가 또 갱신된다면 이는 음수 사이클이 존재한다는 뜻.
    for a, b, w in edges:
        if distances[a] != float('inf') and distances[a]+w < distances[b]:
            return True  # 음수 사이클 존재
    return False


cycle = BellmanFord(1)
if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distances[i] != float('inf'):
            print(distances[i])
        else:
            print(-1)

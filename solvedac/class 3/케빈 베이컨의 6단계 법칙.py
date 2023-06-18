# 알고리즘 - 플로이드 워셜
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
friendship = [[5001]*(n+1) for _ in range(n+1)]
for _ in range(1, m+1):
  a, b = map(int, input().split())
  friendship[a][b] = 1
  friendship[b][a] = 1

for i in range(1, n+1):
  friendship[i][i] = 0 

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      friendship[i][j] = min(friendship[i][j], friendship[i][k] + friendship[k][j])

minNums = [(sum(friendship[i])-5001, i) for i in range(1, n+1)]
minNums.sort(key=lambda x:(x[0], x[1]))
print(minNums[0][1])
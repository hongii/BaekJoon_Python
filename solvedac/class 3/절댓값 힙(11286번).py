import heapq
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
  num = int(input())
  if abs(num) > 0:
    heapq.heappush(hq, (abs(num), num))
  elif num == 0:
    if hq:
      print(heapq.heappop(hq)[1])
    else:
      print(0)
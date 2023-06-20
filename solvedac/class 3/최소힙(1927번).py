import heapq
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
n = int(input())
hq = []
while n:
  n -= 1
  x = int(input())
  if x == 0:
    if hq:
      print(heapq.heappop(hq))
    else:
      print(0)
  else:
    heapq.heappush(hq, x)


# cf) print(int("3\n")) -> 3출력, 따라서 input().rstip()안해도 상관없음
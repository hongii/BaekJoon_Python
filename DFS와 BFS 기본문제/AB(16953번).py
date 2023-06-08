import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

a, b = map(int, input().split())
cnt = 0
while b > a:
  if b % 2 == 0:
    b //= 2
  elif b % 10 == 1:
    b //= 10
  else:
    break
  cnt += 1

if b == a:
  print(cnt+1)
else:
  print(-1)
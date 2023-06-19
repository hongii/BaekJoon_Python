import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
set_n = set()
set_m = set()
for i in range(n):
  name = sys.stdin.readline().rstrip()
  set_n.add(name)

for i in range(m):
  name = sys.stdin.readline().rstrip()
  set_m.add(name)

res = list(set_n & set_m)
res.sort()
print(len(res))
for x in res:
  print(x)
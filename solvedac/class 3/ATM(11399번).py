import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
times = list(map(int, input().split()))
times.sort()
res = 0
for i in range(n):
  res += sum(times[:i+1])
print(res)
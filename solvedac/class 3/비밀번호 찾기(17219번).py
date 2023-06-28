import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
site_pw = {}
for _ in range(n):
  s, pw = input().rstrip().split()
  site_pw[s] = pw

for _ in range(m):
  print(site_pw[input().rstrip()])
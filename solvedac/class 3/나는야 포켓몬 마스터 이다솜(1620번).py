# 그냥 input()으로 받으니까 시간초과 뜸 -> sys.stdin.readline().rstrip()으로 한줄씩 받아오자 (rstrip()은 마지막 개행문자(\n) 제거함)
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
  name = input().rstrip()
  dic[name] = i
  dic[str(i)] = name

for _ in range(m):
  pockemon = input().rstrip()
  print(dic[pockemon])
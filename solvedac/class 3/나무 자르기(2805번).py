# 알고리즘 - 이분탐색
# python3 로 제출 시 시간초과나서 pypy3로 제출함(correct)
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
trees = list(map(int, input().split()))
maxHeight = 0
lt, rt = 1, max(trees)
while lt <= rt:
  mid = (lt+rt) // 2
  cutSize = 0
  for tree in trees:
    if tree-mid > 0:
      cutSize += tree-mid
  if cutSize >= m:
    lt = mid+1
    maxHeight = max(mid, maxHeight)
  elif cutSize < m:
    rt = mid-1
print(maxHeight)
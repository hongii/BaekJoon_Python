import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\대기업 코테 유형\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
numRange = 1
cnt = 1
while n > numRange:
  numRange += 6*cnt
  cnt += 1
print(cnt)
  
# 알고리즘 - 분할정복, 재귀
# 다시 풀기
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n, row, col = map(int, input().split())
cnt = 0

def recZ(start_x, start_y, size):
  global cnt

  if start_x > row or start_y > col or start_x+size < row or start_y+size < col:
    cnt += size**2
    return
  
  if size == 2:
    if start_x == row and start_y == col: # 2사분면
      print(cnt)
      sys.exit()
    cnt += 1
    if start_x == row and start_y+1 == col: # 1사분면
      print(cnt)
      sys.exit()
    cnt += 1
    if start_x+1 == row and start_y == col: # 3사분면
      print(cnt)
      sys.exit()
    cnt += 1
    if start_x+1 == row and start_y+1 == col: # 4사분면
      print(cnt)  
      sys.exit()
    cnt += 1

  else:
    size //= 2
    recZ(start_x, start_y, size) # 2사분면
    recZ(start_x, start_y+size, size) # 1사분면
    recZ(start_x+size, start_y, size) # 3사분면
    recZ(start_x+size, start_y+size, size) # 4사분면

recZ(0, 0, 2**n)
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

T = int(input())
while T:
  T -= 1
  n = int(input())
  f = [()]*(n+1) # idx숫자에 대한 피보나치 재귀함수를 호출했을때의 (0의 갯수, 1의 갯수)쌍을 저장
  if n >= 0:
    f[0] = (1, 0)
  if n >= 1:
    f[1] = (0, 1)
  for i in range(2, n+1):
    f[i] = (f[i-1][0]+f[i-2][0], f[i-1][1]+f[i-2][1])
  print(f[n][0], f[n][1])
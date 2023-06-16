import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\대기업 코테 유형\\input.txt"
sys.stdin = open(filePath, "rt")

while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break

  if max(a, b, c) >= sum([a, b, c]) - max(a, b, c):
    print("Invalid")
  elif a == b == c:
    print("Equilateral")
  elif a != b and a != c and b!= c:
    print("Scalene")
  elif len(set([a, b, c])) == 2:
    print("Isosceles")

import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
s = set()
while n:
  n -= 1
  tmp = input().rstrip()
  if tmp == "all":
    s = set([i for i in range(1, 21)])
  elif tmp == "empty":
    s = set() 
  else:
    op, num = tmp.split()
    num = int(num)
    if op == "add":
      s.add(num)
    elif op == "remove":
      s.discard(num) # set 메서드의 descard()는 집합 s내에 해당 특정 원소가 존재하면 삭제, 존재하지 않으면 무시 -> 특정 요소를 안전하게 삭제
    elif op == "check":
      if num in s:
        print(1)
      else:
        print(0)
    elif op == "toggle":
      if num in s:
        s.remove(num) # set 메서드의 remove()는 집합 s내에 해당 특정 원소가 존재하면 삭제, 존재하지 않으면 error 발생 -> 특정 요소 삭제
      else:
        s.add(num)
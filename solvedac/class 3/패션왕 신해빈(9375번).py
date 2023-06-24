import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

T = int(input())
while T:
  T -= 1
  n = int(input())
  dic = {}
  for _ in range(n):
    [cloth, type] = input().split()
    if type not in dic.keys():
      dic[type] = []
    dic[type].append(cloth)
  
  # 가능한 옷 조합의 수
  res = 1
  for val in dic.values():
    res *= len(val)+1
  print(res-1)


'''
프로그래머스 LV 2 : 의상 문제와 유사
https://github.com/hongii/programmers_python/blob/main/LV%202/%EC%9D%98%EC%83%81.py
'''
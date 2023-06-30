# 맨 처음에 비둘기집 원리 적용 안하고 풀어서 시간초과남, 비둘기집 원리 적용해서 correct
import sys
from itertools import combinations
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

T = int(input())
MBTI = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
cb = list(combinations(MBTI, 2))
dic = {key:0 for key in cb}

# 16가지의 mbti들 중에서 두 mbti 사이의 모든 거리 구하기
for k in dic.keys():
  cnt = 0
  for i in range(4):
    if k[0][i] != k[1][i]:
      cnt += 1
  dic[k] = cnt

# 같은 mbti 유형끼리의 거리는 0으로 설정
for i in range(16):
  dic[(MBTI[i], MBTI[i])] = 0

while T:
  T -= 1
  n = int(input())
  students = list(map(str, input().rstrip().split()))
  if len(students) > 32: # 비둘기집 원리 이용
    print(0)
  else:
    studentsCB = list(combinations(students, 3))
    minDist = 16
    for c in studentsCB:
      dis = 0
      if (c[0], c[1]) in dic.keys():
        dis += dic[(c[0], c[1])]
      else:
        dis += dic[(c[1], c[0])]
      
      if (c[0], c[2]) in dic.keys():
        dis += dic[(c[0], c[2])]
      else:
        dis += dic[(c[2], c[0])]

      if (c[1], c[2]) in dic.keys():
        dis += dic[(c[1], c[2])]
      else:
        dis += dic[(c[2], c[1])]
      
      if dis < minDist:
        minDist = dis
    print(minDist)


'''
# 비둘기집 원리 
=> (n+1)개의 물건을 n개의 상자에 넣을 때 적어도 어느 한 상자에는 두 개 이상의 물건이 들어 있다는 원리

# 문제에 적용하기
=> 16가지 mbti가 있을때 k(k>16)명이 있으면 이 중 같은 mbti를 가지는 사람은 반드시 두 명 이상이다.
따라서, k > 32이면 같은 mbti를 가지는 사람이 반드시 세 명 이상 있다는 것을 알 수 있다.
그러므로 사람이 32명 넘게 있을 때는 무조건 답이 0이 된다. -> 같은 mbti를 가진 세사람의 거리가 가장 최소가 되므로
'''
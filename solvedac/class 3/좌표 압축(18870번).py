# 맨 처음에 문제 이해를 못해서 좌표 압축이 무슨 뜻인지 문제 해설 찾아보고 다시 품
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dic = {key:0 for key in nums}
res = []
numsSet = sorted(list(set(nums)))
for i in range(len(numsSet)):
  dic[numsSet[i]] = i

for x in nums:
  res.append(dic[x])
print(*res)
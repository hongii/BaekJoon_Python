# 알고리즘 - 누적합
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
accNums = [0]*(n+1)
accNums[1] = nums[0]
for i in range(1, n+1):
  accNums[i] = accNums[i-1] + nums[i-1]

while m:
  m -= 1
  i, j = map(int, input().split())
  print(accNums[j]-accNums[i-1])



'''첫번째 코드 -> 시간초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
while m:
  m -= 1
  i, j = map(int, input().split())
  print(sum(nums[i-1:j]))
'''
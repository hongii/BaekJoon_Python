# 알고리즘 :  수학, 사칙연산
import math
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\대기업 코테 유형\\input.txt"
sys.stdin = open(filePath, "rt")

H, W, N, M = map(int, input().split())
cntW = math.ceil(W / (M+1))
cntH = math.ceil(H / (N+1))
print(cntH*cntW)

# 정석 풀이는 KMP 알고리즘을 이용하는 풀이..그러나 파이썬은 문자열의 신이다?
# 백준 골4 문제로 보고 풀었는데 브론즈2까지 떨어져있었음
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
inputStr = input()
subStr = input()

if subStr in inputStr:
    print(1)
else:
    print(0)

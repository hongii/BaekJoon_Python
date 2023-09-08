### 투 포인터 문제 ###

# 1회차 코드
# import sys
# filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
# sys.stdin = open(filePath, "rt")
# n, s = map(int, input().split())
# numList = list(map(int, input().split()))

# lp, rp = 0, 0
# tmpSum, res = 0, 100001 # tmpSum은 nunmList[lp:rp]까지의 합(numList[rp]의 값은 포함하지 않음!)
# while True:
#     if tmpSum >= s:
#         res = min(res, rp-lp)
#         tmpSum -= numList[lp]
#         lp += 1
#     elif rp == n:
#         break
#     else:
#         tmpSum += numList[rp]
#         rp += 1

# if res == 100001:
#     print(0)
# else:
#     print(res)

'''
PS. (아....문제 제대로 좀 읽자................)
"이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구해야 하는 문제"인데..
계속 그 합이 S와 같을때만 그 길이를 갱신해버려서 자꾸 wrong answer가 뜸
이상 이상 이상 이상...이상이요..값이 동일할 때만 res를 갱신 하는게 아니라 연속된 수열의 합이 S 이상!!!일 때 전부 갱신해야함

그리고 부분합 초기값 설정에 따라 tmpSum을 비교하는 순서가 중요!
해당 문제 다시 풀어보기
'''

####################################################################################################################
# 2회차 코드
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline
n, s = map(int, input().split())
numList = list(map(int, input().split()))

lp, rp = 0, 0
tmpSum, res = 0, n

for lp in range(n):
    while tmpSum < s and rp < n:
        tmpSum += numList[rp]
        rp += 1

    if tmpSum >= s and res > rp - lp:
        res = rp - lp

    tmpSum -= numList[lp]

print(res)

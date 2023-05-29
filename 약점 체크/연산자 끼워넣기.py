from itertools import permutations
# import sys
# filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
# sys.stdin = open(filePath, "rt")
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "//":
        if num1 < 0:
            return -(-num1//num2)
        else:
          return num1 // num2
    
ops_dic = {"+":ops[0], "-":ops[1], "*":ops[2], "//":ops[3]}
opsList = []
for key, value in ops_dic.items():
    for i in range(value):
      opsList.append(key)

pm = list(set(permutations(opsList, len(opsList))))
ans = []
for x in pm:
    res = nums[0]
    for i in range(1, len(nums)):
        res = calculate(res, nums[i], x[i-1])
    ans.append(res)
ans.sort()
print(ans[-1])
print(ans[0])
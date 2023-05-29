### sol1) itertools라이브러리에서 permutaions 사용한 풀이 -> 시간이 좀 더 걸린다(584ms)###
from itertools import permutations
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



### sol2) dfs 이용한 백트래킹 풀이 -> 순열 라이브러리 사용시 보다 시간이 좀 더 줄어든다(96ms) ###
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
ops_dic = {"+":ops[0], "-":ops[1], "*":ops[2], "//":ops[3]}
ans = []

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

def dfs(i, res, opstr):
    if i == len(nums):
        ans.append(res)
        # print(opstr, res)
    else:
        for key, value in ops_dic.items():
            if value > 0:
                preRes = res
                res = calculate(res, nums[i], key)
                ops_dic[key] -= 1
                # preStr = opstr
                opstr += key + str(nums[i])
                dfs(i+1, res, opstr)
                ops_dic[key] += 1
                # opstr = preStr
                res = preRes

dfs(1, nums[0], str(nums[0]))
ans.sort()
print(ans[-1])
print(ans[0])
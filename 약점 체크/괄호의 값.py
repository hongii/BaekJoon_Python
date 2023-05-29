# 두번째 코드 -> 정답 풀이 참고
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
brackets = input()
stack = []
tmp, res = 1, 0
for i, b in enumerate(brackets):
    if b == "(":
        tmp *= 2
        stack.append(b)
    elif b == "[":
        tmp *= 3
        stack.append(b)
    elif b == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        elif brackets[i-1] == "(":
            res += tmp
        tmp //= 2
        stack.pop()
    elif b == "]":
        if not stack or stack[-1] == "(":
            res = 0
            break
        elif brackets[i-1] == "[":
            res += tmp
        tmp //= 3
        stack.pop()

# 아래의 코드 없이 그냥 print(res)만 했을 때 틀린 답이 도출
# ex) 위의 코드에서 break 없이 통과되었지만 stack에 괄호가 남아있는 경우의 반례 -> ((((([]
# 참고로 올바른 괄호가 주어진 경우, 위의 코드 수행했을 때 break에 걸리지 않으면서 stack이 비어있어야 한다.
if stack:
    print(0)
else:
    print(res)





''' 첫번째 코드 -> 예제는 통과, 코드 제출시 valueError 런타임에러 발생...해결 못함
stack = []
brackets = input()
isEmpty = 0
for b in brackets:
    if b == ")":
        tmp = "("
        while stack and stack[-1] != "(":
            tmp += stack.pop() + " "
        if not stack:
            isEmpty = 1
            break
        stack.pop()
        tmp += ")"
        if tmp == "()":
            stack.append("2")
        else:
            tmp = tmp[1:-2]
            addNum = 0
            for num in tmp.split():
                addNum += int(num)
            stack.append(str(addNum*2))
    
    elif b == "]":
        tmp = "["
        while stack and stack[-1] != "[":
            tmp += stack.pop() + " "
        if not stack:
            isEmpty = 1
            break    
        stack.pop()
        tmp += "]"
        if tmp == "[]":
            stack.append("3")
        else:
            tmp = tmp[1:-2]
            addNum = 0
            for num in tmp.split():
                addNum += int(num)
            stack.append(str(addNum*3))
    
    else:
        stack.append(b)

res = 0
if not isEmpty:
    while stack:
        res += int(stack.pop())
    print(res)
else:
    print(0)

'''
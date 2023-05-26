T = int(input())
while T:
    res = []
    n = int(input())
    binaryNum = bin(n)[2:]
    binaryNum = binaryNum[::-1]
    for i in range(len(binaryNum)):
        if binaryNum[i] == "1":
            res.append(i)
    print(*res)
    T -= 1
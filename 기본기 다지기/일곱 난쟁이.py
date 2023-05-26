inputNums = [int(input()) for _ in range(9)]
gap = sum(inputNums) - 100
check = 0
for i in range(len(inputNums)):
    num = inputNums[i]
    for j in range(i+1, len(inputNums)):
        if inputNums[i] + inputNums[j] == gap:
            remove1, remove2 = inputNums[i], inputNums[j]
            inputNums.remove(remove1)
            inputNums.remove(remove2)
            check = 1
            break
    if check:
        break
for x in sorted(inputNums):
    print(x)
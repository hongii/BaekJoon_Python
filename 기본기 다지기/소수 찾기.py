n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(len(nums)):
    if nums[i] == 1:
        continue
    for j in range(2, int(nums[i]**0.5)+1):
        if nums[i] % j  == 0:
            break
    else:
        cnt += 1
print(cnt)
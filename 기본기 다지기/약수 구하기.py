n, k = map(int, input().split())
res = []
for i in range(1, n+1):
    if n % i == 0:
        res.append(i)
if len(res) < k:
    res = 0
print(res[k-1] if res != 0 else res)
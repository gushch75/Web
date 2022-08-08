a = list(map(int, input().split()))
minElem = min(a)
b = a.copy()
b.sort()
maxElem = minElem
print(b)
for i in range(1, len(b)):
    if b[i] <= b[i - 1] + 1:
        maxElem += b[i] - b[i - 1]
    else:
        break
answer = [minElem, maxElem]
print(answer)
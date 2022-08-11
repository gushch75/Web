s = input()  # 256+895*986/3-4293/294-1 --------- 294397,0646258504
s = ' ' + s
s1 = '+-*/'
s11 = '*/'
s2 = ''
a = 0
b = 0
f = []
for x in range(len(s)):
    if s[x] in s1:
        if a + 1 == x:
            f.append(int(s[x]))
            s2 = s2 + str(b) + s[x]
            b += 1
        else:
            f.append(int(s[a + 1:x]))
            s2 = s2 + str(b) + s[x]
            b += 1
        a = x
f.append(int(s[a + 1:x + 1]))
s2 = s2 + str(b)
# print(s2)
print(f)
for x in range(1, len(s2), 2):
    if s2[x] in s11:
        a = 1
        if s2[x] == '*' and a == 1:
            c = f[int(x // 2)] * f[int((x // 2) + 1)]
            f[(x // 2)] = 0
            f[(x // 2) + 1] = c
            a += 1
        elif s2[x] == '*' and a > 1:
            d = c * f[int(x // 2 + 1)]
            f[(x // 2)] = 0
            f[(x // 2) + 1] = d
            c = d
            a += 1
        elif s2[x] == '/' and a == 1:
            c = f[int(x // 2)] / f[int((x // 2) + 1)]
            f[(x // 2)] = 0
            f[(x // 2) + 1] = c
            a += 1
        elif s2[x] == '/' and a > 1:
            d = c / f[int((x // 2) + 1)]
            f[(x // 2)] = 0
            f[(x // 2) + 1] = d
            c = d
            a += 1
    else:
        a = 0
import copy

# print(f)
z = copy.deepcopy(f)
for x in range(1, len(s2), 2):
    if s2[x] == '+':
        z[x // 2] = 1
    elif s2[x] == '-':
        z[x // 2] = 2
while 0 in f or 0 in z:
    f.remove(0)
    z.remove(0)
rez = f[0]
# print(s2)
# print(f)
# print(z)
for x in range(1, len(z), 1):
    if z[x - 1] == 1:
        rez = rez + f[x]
    elif z[x - 1] == 2:
        rez = rez - f[x]
print(rez)
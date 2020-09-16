a = int(input(""))
b = int(input(""))
minnum = min(a, b)
maxnum = max(a, b)
qtdodd = 0
for i in range(minnum, maxnum+1, 1):
    if i%2 > 0:
        qtdodd = qtdodd + 1

print(qtdodd)
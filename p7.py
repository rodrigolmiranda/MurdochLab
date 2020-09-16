x = int(input(""))
y = int(input(""))
minnum = min(x, y)
maxnum = max(x, y)

for i in range(minnum, maxnum, 1):
    if i%5 in (2, 3):
        print(i)


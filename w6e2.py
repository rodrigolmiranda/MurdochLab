a = input("")
p = 1
size = len(a)
for i in range(int(size / 2)):
    if a[i] != a[size - 1 - i]:
        print(0)
        p = 0
        break

if p == 1:
    print(1)

a = input("")
a = a.lower()
ret = ""
for i in range(len(a)) :
    if (a[i] in ("a", "e", "i", "o", "u") and a[i] not in ret):
        ret = ret + a[i]

print(ret)

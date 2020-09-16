n = int(input(""))
out = ""
c = 1
for i in range(1, n+1, 1):
    out = out + str(c) + " " + str(c+1) + " " + str(c+2) + " EFFAT"
    c = c + 4
    print(out)
    out = ""

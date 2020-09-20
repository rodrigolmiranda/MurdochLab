# %%
import datetime

ini = datetime.datetime.now()


def isPrime(n, l=[]):
    flag = True
    if n != 2 and n % 2 == 0:
        return False

    if len(l) == 0:
        lint = list(range(1, int(n/2), 2))
    else:
        if l[-1]+2 < int(n/2):
            lint = l + list(range(l[-1]+2, int(n/2), 2))
        else:
            lint = list(filter(lambda x: x <= int(n/2), l))
            if 1 in lint:
                lint.remove(1)

    for i in lint:
        if n % i == 0:
            flag = False
            break

    if flag and n not in lPr:
        lPr.append(n)

    return flag


global lPr
lPr = [1]

N = 10000
R = [1]

for i in range(2, N+1, 1):
    a = isPrime(i, lPr)
    if a and i not in R:
        R.append(i)

# print("RRR", R)
# print("lPr", lPr)

print(datetime.datetime.now()-ini)

# %%

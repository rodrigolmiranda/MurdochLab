def isPrime(n):
    flag=True
    for i in range(2, n-1):
        if n%i==0:
            flag=False
            break
    return flag

N = 1000
R = []
for i in range(1, N):
    if isPrime(i):
        R.append(i)
print(R)

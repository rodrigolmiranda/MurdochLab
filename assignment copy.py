def gcd(a, b):
    if (b == 0):
        return a
    else:
        #print(a, b, a % b)
        return gcd(b, a % b)

# 2147483647 #-2147483648
#r =int((2147483647**0.5)-1) #print(r)
print(gcd(34, 20))
"""
p = 43
q = 23
N = 764
"""
p = 11
q = 3
n = 33
yn = (p-1)*(q-1)
yp = p-1
r = 1
print(gcd(3, yn))

"""
for i in range(q):
    r = (r*p)%n
print(r)
"""
"""





#####################################
v = ("a", "e", "i", "o", "u")
a = input("")
ret = []
for i in a.lower() :
    if (i in v and i not in ret):
        ret.append(i)

print(ret)
#####################################

x = 43
y = 23
N = 764
r = 1
for i in range(y):
    r = (r*x)%N
print(r)
#####################################

p2=0
p1=1
n = 28
result = []
result.append(p2)
result.append(p1)
for i in range(n):
    current = p2+p1
    result.append(current)
    #print(current)
    p2 = p1
    p1 = current

print(result)
v = int(input())
print(v)
print(v in result)

#####################################

n=int(input("Your Number: "))
p2=0
p1=1
L=[]
L.append(p2)
L.append(p1)
current=1
while current<n:
    current=p2+p1
    L.append(current)
    p2=p1
    p1=current
print(L)
print(n in L)
#####################################
#generate a 10 digit fib number
n=999999999
p2=0
p1=1
L=[]
L.append(p2)
L.append(p1)
current=1
while current<n:
    current=p2+p1
    L.append(current)
    p2=p1
    p1=current
print(L[-1])
#print(n in L)
"""

#generate a 10 digit fib number
n=999999999
p2=0
p1=1
L=[]
L.append(p2)
L.append(p1)
current=1
while current<n:
    current=p2+p1
    L.append(current)
    p2=p1
    p1=current
print(L[-1])
#print(n in L)